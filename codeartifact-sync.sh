#!/usr/bin/env bash

set -euo pipefail

SOURCE_REGION="us-east-1"
DEST_REGION="us-east-2"

DOMAIN="my-domain"
OWNER="123456789012"

TMPDIR=$(mktemp -d)
trap 'rm -rf "$TMPDIR"' EXIT

echo "Getting repositories..."

repos=$(aws codeartifact list-repositories-in-domain \
    --domain "$DOMAIN" \
    --domain-owner "$OWNER" \
    --region "$SOURCE_REGION" \
    --query 'repositories[].name' \
    --output text)

for repo in $repos; do
    echo "================================================="
    echo "Repository: $repo"

    formats=$(aws codeartifact list-packages \
        --domain "$DOMAIN" \
        --domain-owner "$OWNER" \
        --repository "$repo" \
        --region "$SOURCE_REGION" \
        --query 'packages[].format' \
        --output text | tr '\t' '\n' | sort -u)

    for format in $formats; do

        packages=$(aws codeartifact list-packages \
            --domain "$DOMAIN" \
            --domain-owner "$OWNER" \
            --repository "$repo" \
            --region "$SOURCE_REGION" \
            --query "packages[?format=='$format'].package" \
            --output text)

        for package in $packages; do
            echo "Package: $package ($format)"

            versions=$(aws codeartifact list-package-versions \
                --domain "$DOMAIN" \
                --domain-owner "$OWNER" \
                --repository "$repo" \
                --format "$format" \
                --package "$package" \
                --region "$SOURCE_REGION" \
                --query 'versions[].version' \
                --output text)

            for version in $versions; do
                echo "  Version: $version"

                assets=$(aws codeartifact list-package-version-assets \
                    --domain "$DOMAIN" \
                    --domain-owner "$OWNER" \
                    --repository "$repo" \
                    --format "$format" \
                    --package "$package" \
                    --package-version "$version" \
                    --region "$SOURCE_REGION" \
                    --query 'assets[].name' \
                    --output text)

                for asset in $assets; do
                    file="$TMPDIR/$asset"

                    echo "    Downloading $asset"

                    aws codeartifact get-package-version-asset \
                        --domain "$DOMAIN" \
                        --domain-owner "$OWNER" \
                        --repository "$repo" \
                        --format "$format" \
                        --package "$package" \
                        --package-version "$version" \
                        --asset "$asset" \
                        --region "$SOURCE_REGION" \
                        "$file"

                    echo "    Uploading $asset"

                    aws codeartifact publish-package-version \
                        --domain "$DOMAIN" \
                        --domain-owner "$OWNER" \
                        --repository "$repo" \
                        --format "$format" \
                        --package "$package" \
                        --package-version "$version" \
                        --asset-content "$file" \
                        --asset-name "$asset" \
                        --asset-sha256 "$(sha256sum "$file" | awk '{print $1}')" \
                        --unfinished \
                        --region "$DEST_REGION"
                done

                aws codeartifact update-package-versions-status \
                    --domain "$DOMAIN" \
                    --domain-owner "$OWNER" \
                    --repository "$repo" \
                    --format "$format" \
                    --package "$package" \
                    --versions "$version" \
                    --target-status Published \
                    --region "$DEST_REGION"
            done
        done
    done
done

echo "Done."

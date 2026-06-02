#!/usr/bin/env python3
import click

from number_ops import _add_num
from network_ops import _add_ip

@click.group(invoke_without_command=True, chain=True)
def cli():
    pass


# Option to Add Numbers
@cli.command()
@click.option("-n", "--num1", required=True)
@click.option("-m", "--num2", required=True)
def add_numbers(num1, num2):
    """Add Numbers"""
    _add_num(
        num1,
        num2,
    )


# Option to take and test IP Addresses
@cli.command()
@click.option("-i", "--ip-addresses", required=True)
def add_ip_addresses(ip_addresses):
    """Add IP Addresses"""
    ip_addresses_list = ip_addresses.split(",") if ip_addresses else []
    _add_ip(
        ip_addresses_list,
    )



if __name__ == '__main__':
    cli()

const form = document.getElementById("item-form");
const itemId = document.getElementById("item-id");
const nameInput = document.getElementById("name");
const descriptionInput = document.getElementById("description");

const formTitle = document.getElementById("form-title");
const cancelButton = document.getElementById("cancel-button");
const itemsContainer = document.getElementById("items-container");
const message = document.getElementById("message");


document.addEventListener("DOMContentLoaded", () => {
    loadItems();
});


function showMessage(text, error = false) {
    message.textContent = text;

    message.className = error
        ? "message-error"
        : "message-success";

    setTimeout(() => {
        message.textContent = "";
        message.className = "";
    }, 3000);
}


async function loadItems() {
    itemsContainer.innerHTML = "Loading...";

    try {
        const response = await fetch("/api/items");

        if (!response.ok) {
            throw new Error("Failed to load items");
        }

        const items = await response.json();

        renderItems(items);

    } catch (error) {
        itemsContainer.innerHTML =
            `<p class="message-error">${error.message}</p>`;
    }
}


function renderItems(items) {

    if (items.length === 0) {
        itemsContainer.innerHTML = "<p>No items found.</p>";
        return;
    }

    itemsContainer.innerHTML = items.map(item => `
        <div class="item">

            <h3>${escapeHtml(item.name)}</h3>

            <p>${escapeHtml(item.description || "")}</p>

            <div class="item-actions">

                <button
                    class="secondary"
                    onclick="editItem(${item.id})"
                >
                    Edit
                </button>

                <button
                    class="danger"
                    onclick="deleteItem(${item.id})"
                >
                    Delete
                </button>

            </div>

        </div>
    `).join("");
}


form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const id = itemId.value;

    const payload = {
        name: nameInput.value.trim(),
        description: descriptionInput.value.trim()
    };

    if (!payload.name) {
        showMessage("Name is required", true);
        return;
    }

    try {

        const response = await fetch(
            id ? `/api/items/${id}` : "/api/items",
            {
                method: id ? "PUT" : "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(payload)
            }
        );

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Request failed");
        }

        showMessage(
            id ? "Item updated successfully" : "Item created successfully"
        );

        resetForm();
        loadItems();

    } catch (error) {
        showMessage(error.message, true);
    }
});


async function editItem(id) {

    try {

        const response = await fetch(`/api/items/${id}`);

        const item = await response.json();

        if (!response.ok) {
            throw new Error(item.error || "Failed to load item");
        }

        itemId.value = item.id;
        nameInput.value = item.name;
        descriptionInput.value = item.description || "";

        formTitle.textContent = "Edit Item";
        cancelButton.classList.remove("hidden");

        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });

    } catch (error) {
        showMessage(error.message, true);
    }
}


async function deleteItem(id) {

    if (!confirm("Are you sure you want to delete this item?")) {
        return;
    }

    try {

        const response = await fetch(`/api/items/${id}`, {
            method: "DELETE"
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Delete failed");
        }

        showMessage("Item deleted successfully");

        loadItems();

    } catch (error) {
        showMessage(error.message, true);
    }
}


cancelButton.addEventListener("click", () => {
    resetForm();
});


function resetForm() {
    form.reset();

    itemId.value = "";

    formTitle.textContent = "Create Item";

    cancelButton.classList.add("hidden");
}


function escapeHtml(value) {
    return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
}

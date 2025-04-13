// Pass the object list from Django to JavaScript
document.addEventListener("DOMContentLoaded", function() {
    const itemsPerPage = 5;

    const paginators = document.querySelectorAll(".paginator");
    for (const paginator of paginators) {
        const container = paginator.querySelector(".object-list")
        const objectList = Array.from(container.children);
        let currentPage = 1;

        function renderList(page)
        {
            const startIndex = (page - 1) * itemsPerPage;
            const endIndex = startIndex + itemsPerPage;
            const currentItems = objectList.slice(startIndex, endIndex);

            // Clear the current list content
            container.innerHTML = "";

            // Render the current page of objects
            currentItems.forEach(item => {
                container.appendChild(item);
            });

            updatePaginationControls(page);
        }

        function updatePaginationControls(page)
        {
            const totalPages = Math.ceil(objectList.length / itemsPerPage);
            const paginationContainer = paginator.querySelector(".pagination");

            // Clear existing page numbers
            while (paginationContainer.children.length > 2) {
                paginationContainer.removeChild(paginationContainer.children[1]);
            }

            // Add page numbers dynamically
            for (let i = 1; i <= totalPages; i++) {
                const pageItem = document.createElement("li");
                pageItem.classList.add("page-item");

                const pageButton = document.createElement("button");
                pageButton.classList.add("page-link");
                pageButton.textContent = i;
                pageButton.type = "button";
                pageButton.addEventListener("click", () => {
                    currentPage = i;
                    renderList(currentPage);
                });

                if (i === page) {
                    pageItem.classList.add("active");
                }

                pageItem.appendChild(pageButton);
                paginationContainer.insertBefore(pageItem, paginationContainer.querySelector(".next-btn").parentElement);
            }

            // Disable prev/next buttons when on first/last page
            paginationContainer.querySelector(".prev-btn").classList.toggle("disabled", page === 1);
            paginationContainer.querySelector(".next-btn").classList.toggle("disabled", page === totalPages);
        }

        // Pagination Button Handlers
        paginator.querySelector(".prev-btn").addEventListener("click", () => {
            if (currentPage > 1) {
                currentPage--;
                renderList(currentPage);
            }
        });

        paginator.querySelector(".next-btn").addEventListener("click", () => {
            const totalPages = Math.ceil(objectList.length / itemsPerPage);
            if (currentPage < totalPages) {
                currentPage++;
                renderList(currentPage);
            }
        });

        document.addEventListener("submit", (event) => {
            event.preventDefault();

            container.innerHTML = "";

            for (const item of objectList)
            {
                if (item.querySelector("input").checked)
                {
                    container.appendChild(item);
                }
            }

            event.target.submit();
        })

        // Initial render
        renderList(currentPage);
    }
});

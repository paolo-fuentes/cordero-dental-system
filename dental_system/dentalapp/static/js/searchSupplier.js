const searchField = document.querySelector('#searchField');

const tableOutput = document.querySelector('.table-output');
const appTable = document.querySelector('.app-table');
tableOutput.style.display = 'none';
const tbody = document.querySelector(".table-body");

searchField.addEventListener('keyup', (e) => {
    const searchValue=e.target.value;

    if(searchValue.trim().length > 0) {
        console.log("searchValue", searchValue);
        tbody.innerHTML = "";

        fetch("/search-supplier", {
            body: JSON.stringify({searchText: searchValue}),
            method: "POST"
        })
            .then((res) => res.json())
            .then((data) => {
                console.log("data", data)
                appTable.style.display = "none";
                tableOutput.style.display = "block";

                if(data.length === 0){
                    tableOutput.style.display = "none";
                }else{
                    data.forEach((item) => {
                        tbody.innerHTML +=`
                            <tr>

                            <td data-heading="Contact Person">${item.contact_person}</td>
                            <td data-heading="Contact Number">${item.contact_number}</td>
                            <td data-heading="Address Line 1">${item.address1}</td>
                            <td>
                                <a class="" href="{% url 'dentalapp:supplier_update' supplier.id %}"><i class="fas fa-edit fa-2x" style="color:black"></i></a>
                            </td>
                            <td>
                                <!--{% csrf_token %}-->
                                <!-- <form action="{% url 'dentalapp:supplier_delete' supplier.id %}" method='post'> -->
                                    <!--<button type = 'submit' class='btn'>-->
                                        <a class="" href="{% url 'dentalapp:supplier_delete' supplier.id %}"><i class="fas fa-trash-alt fa-2x" style="color:black"></i></a>
                                    <!--</button>-->
                                </form>
                            </td>


                            </tr>`;
                    });

                }
            });
    }else{
        tableOutput.style.display = "none";
        appTable.style.display = "block";
    }



});
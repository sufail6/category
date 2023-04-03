{% extends 'home.html' %}
{% load static %}
{% block content %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
<script src="https://code.jquery.com/jquery-3.6.4.js" integrity="sha256-a9jBBRygX1Bh5lt8GZjXDzyOB+bWve9EiO7tROUtj/E=" crossorigin="anonymous"></script>

<table class="table">
  <thead>
    <tr>
      <th scope="col">NAME</th>
      <th scope="col">STATUS</th>
        <th scope="col" colspan="3">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Action</th>

      <th><a href="{% url 'catform' %}"><button scope="col" type="button" class="btn btn-success">Add Category</button></a></th>
    </tr>
  </thead>
  <tbody>
  {% for d in personal %}
    <tr><th scope="row">{{d.Name}}</th>
        <th>
        {% if d.is_active == True  %}
            Disable
            {% else %}
            enable
            {% endif %}
        </th><td><a href="{% url 'updatecat' d.id %}"><button type="button" class="btn btn-sm btn-warning">EDIT</button></a></td>
            <td><button onclick="disable()" type="button" class="btn btn-info">DISABLE</button></td>
            <td><a href="{% url 'disable' d.id %}"><button type="button" class="btn btn-primary">ENABLE</button></a></td>
    </tr>
    </tr>
    </tbody>
    {% endfor %}
</table>
<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
<script>
        function disable() {
            const swalWithBootstrapButtons = Swal.mixin({
  customClass: {
    confirmButton: 'btn btn-success',
    cancelButton: 'btn btn-danger'
  },
  buttonsStyling: false
})

swalWithBootstrapButtons.fire({
  title: 'Are you sure?',
  text: "You won't be able to revert this!",
  icon: 'warning',
  showCancelButton: true,
  confirmButtonText: 'Yes, delete it!',
  cancelButtonText: 'No, cancel!',
  reverseButtons: true
}).then((result) => {
  if (result.isConfirmed) {
    swalWithBootstrapButtons.fire(
      'Deleted!',
      'Your file has been deleted.',
      'success'
    )
  } else if (
    / Read more about handling dismissals below /
    result.dismiss === Swal.DismissReason.cancel
  ) {
    swalWithBootstrapButtons.fire(
      'Cancelled',
      'Your imaginary file is safe :)',
      'error'
    )
  }
})

        }

    </script>




{% endblock content %}
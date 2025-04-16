<br />
<div align="center">
  <h3 align="center">Kitchen service</h3>

  <p align="center">
    Manage kitchen deliverables
    <br />
    <a href="https://github.com/Windings-Lab/kitchen-service"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Windings-Lab/kitchen-service">View Demo</a>
    &middot;
    <a href="https://github.com/Windings-Lab/kitchen-service/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/Windings-Lab/kitchen-service/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Here as a cook you can create new dishes based on your ingredients and dish types. And you can also set cooks to be responsible for this or another dish


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Django][DjangoProject.com]][Django-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python 3.13
```sh
  python pip install -r requirements.txt
```

### Optional

1. Install database data
```sh
  python manage.py loaddata .\json\dump.json;
```

2. Login with
```
Username: admin
Password: admin
```

### Environment

```dotenv
# DB
PGDATABASE # PostgreSQL DB
PGUSER # PostgreSQL User
PGPASSWORD # PostgreSQL Password
PGHOST # PostgreSQL Host
PGPORT # PostgreSQL Port

# Django
DJANGO_SETTINGS_MODULE
DJANGO_SECRET_KEY
RENDER_EXTERNAL_HOSTNAME

# Storage
B2_KEY_ID # Backblaze key id
B2_APP_KEY # Backblaze app key
B2_BUCKET_NAME # Backblaze bucket name
B2_ENDPOINT_URL # Backblaze endpoint
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[DjangoProject.com]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green
[Django-url]: https://www.djangoproject.com/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com

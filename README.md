# Django Job

The Django Salon Appointment Management System is a web-based application designed to streamline how customers book, manage, and pay for salon services without using physical cash. The platform ensures a seamless user experience, allowing customers to schedule appointments, select services, make payments through a digital wallet, and provide feedback — all from the convenience of their devices.

### Getting Started

These instructions will guide you through setting up Django Salon on your local machine for development and testing purposes. This guide assumes you are working on a Windows environment. Mac and Linux users can adapt the commands accordingly.

### Prerequisites

Below are the dependencies for the project. For quicker installation, please refer to the [requirements.txt](requirements.txt) file.
- [Python](https://www.python.org/downloads/) - The programming language used to build the backend of the application.
- [Django](https://www.djangoproject.com/download/) - The web framework that powers the server-side logic, database models, and URL routing.
- [Visual Studio Code](https://code.visualstudio.com/) -  A lightweight, flexible code editor recommended for writing and managing the project code.
- [Django Widget Tweaks](https://pypi.org/project/django-widget-tweaks/) - A Django template tag library used to customize form fields directly in templates.
- [Django Filter](https://pypi.org/project/django-filter/) - Adds filtering capabilities to Django views, making it easy to implement search and filter functionality.
- [Requests](https://pypi.org/project/requests/) - A simple and elegant HTTP library for Python, used to send HTTP/1.1 requests with methods like GET and POST. It simplifies interacting with external APIs.

### Installing

Create and initialize a virtual environment (optional)

    pip install virtualenv
    virtualenv salon_env
    cd salon_env
    Scripts\activate

Clone the Repository

    clone https://github.com/chidiohiri/django-salon.git
    cd django-salon

Move the project into the virtual environment, then install dependencies. The project dependencies can found in [requirements.txt](requirements.txt)

    pip install -r requirements.txt

Migrate all tables to the Sqlite3 DB

    python manage.py makemigrations
    python manage.py migrate

Create/Login to Paystack account, and get secret and public key, then add it to the settings.py file (see file ending)

    PAYSTACK_SECRET_KEY = ''
    PAYSTACK_PUBLIC_KEY = ''

Create a super user. This account will be used to access the admin dashboard and verify objects.

    python manage.py createsuperuser

Run server on your terminal (cmd or powershell). Open your browser and navigate to http://127.0.0.1:8000/ to access the application.

    python manage.py runserver

### Core Features

- Cashless Transactions: Customers load money into their in-app Wallet and use it to pay for appointments instantly. This eliminates the need for handling physical cash at the salon.

- Service Selection and Dynamic Pricing: Customers can select multiple services during booking. The system automatically calculates the total service cost before checkout.

- Appointment Scheduling and Management: Users can easily book appointments by choosing preferred services and dates. They can also update or cancel future appointments directly from their dashboard.

- Wallet Management: Each user has a Wallet tied to their profile. When an appointment is scheduled, the system checks for sufficient wallet balance, deducts the amount, and processes the booking.

- Refunds on Cancellations: If a customer cancels an appointment before the scheduled date, the system automatically refunds the appointment cost back into their Wallet.

- Real-time Status Tracking: Appointments are labeled based on their date: Today, Past, or Upcoming to help users easily track their bookings.

- Customer Feedback Collection: After a service is completed, customers can submit feedback, helping the salon improve service quality.

- Salon Control: Administrators or barbers can cancel available days, preventing customers from scheduling appointments on those days and maintaining operational flexibility.

### Deployment

For production deployment, you will need to configure your application with a production-grade database (such as PostgreSQL), static file handling, and secure hosting. You may refer to the official [Django Documentation](https://docs.djangoproject.com/en/5.1/howto/deployment/) on deployment

### Authors

  - **Chidi Ohiri** - *For updates, networking, or feedback, feel free to connect:* -
    [Linkedin](https://www.linkedin.com/in/chidiebere-ohiri/)

### License

This project is licensed under the [MIT LICENSE](LICENSE.md), which permits reuse, modification, and distribution with proper attribution.

### Acknowledgments

  - Guido van Rossum, the creator of Python
  - The Django core team and community for building and maintaining such a robust framework
  - Developers and open-source contributors whose work inspired or supported the development of this project


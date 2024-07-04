# 🚀 Custom Invoice Module for Odoo 17

Welcome to the **Custom Invoice Module** for Odoo 17! This module extends the default invoice functionality by adding several useful fields and features, perfect for tech companies.

## 📋 Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## 📝 Overview

The **Custom Invoice Module** enhances your invoicing process with additional fields and stylish templates. It's designed to provide tech companies with more flexibility and information in their invoices.

## ⚙️ Installation

To install the module, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/jmillanstem/odoo17-addons.git
    cd odoo17-addons
    ```

2. **Copy the addons to your Odoo addons directory**:
    ```bash
    cp -r custom_invoice /path/to/your/odoo/addons/
    ```

3. **Update your Odoo configuration**:
    Add the path to your addons directory in the `odoo.conf` file:
    ```ini
    [options]
    addons_path = /path/to/your/odoo/addons,/path/to/odoo17-addons/custom_invoice
    ```

4. **Restart Odoo**:
    ```bash
    sudo systemctl restart odoo
    ```

5. **Update Apps List**:
    - Go to `Apps` in Odoo.
    - Click on `Update Apps List`.
    - Search for `Custom Invoice Module`.
    - Click on `Install`.

## 🚀 Usage

Once installed, you can use the new fields and features in your invoices:

1. **Log in to your Odoo instance**.
2. **Navigate to Invoices** under the Accounting module.
3. **Create or edit an invoice** and you'll see new fields such as `Additional Information`, `Custom Date`, `Project URL`, `Project Manager`, `Project Status`, `Detailed Description`, `Internal Notes`, and `Delivery Date`.

## 🌟 Features

- **Additional Information**: Add extra details to your invoices.
- **Custom Date**: Specify a custom date for your records.
- **Project URL**: Link invoices to specific projects.
- **Project Manager**: Assign a project manager to each invoice.
- **Project Status**: Track the status of the related project.
- **Detailed Description**: Add detailed notes or descriptions.
- **Internal Notes**: Include internal comments not shown on the printed invoice.
- **Delivery Date**: Set a delivery date for the project or service.

## 📸 Screenshots

![Invoice Form](https://via.placeholder.com/800x400?text=Invoice+Form+with+Custom+Fields)
*Figure 1: Invoice form with additional fields*

![Invoice PDF](https://via.placeholder.com/800x400?text=Custom+Styled+Invoice+PDF)
*Figure 2: Custom styled invoice PDF with additional information*

## 🤝 Contributing

Contributions are welcome! To contribute:

1. **Fork the repository**.
2. **Create a new branch**:
    ```bash
    git checkout -b feature-branch
    ```
3. **Make your changes**.
4. **Commit your changes**:
    ```bash
    git commit -m "Add new feature"
    ```
5. **Push to the branch**:
    ```bash
    git push origin feature-branch
    ```
6. **Create a pull request**.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

For any questions or inquiries, please contact:

- **Jaime Millán**
- **Company**: Stemdo
- **Email**: jmillan@stemdo.io
- **GitHub**: [jmillanstem](https://github.com/jmillanstem)

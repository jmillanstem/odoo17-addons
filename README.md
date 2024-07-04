# 🛠️ Odoo 17 Addons

This repository contains custom addons for Odoo 17. These modules enhance the functionality of Odoo by providing additional features and improvements.

## 📋 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## 🛠️ Installation

To install the addons in this repository, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/jmillanstem/odoo17-addons.git
    cd odoo17-addons
    ```

2. **Copy the addons to your Odoo addons directory**:
    ```bash
    cp -r addons/* /path/to/your/odoo/addons/
    ```

3. **Update your Odoo configuration**:
    Add the path to your addons directory in the `odoo.conf` file:
    ```ini
    [options]
    addons_path = /path/to/your/odoo/addons,/path/to/odoo17-addons/addons
    ```

4. **Restart Odoo**:
    ```bash
    sudo systemctl restart odoo
    ```

## 🚀 Usage

To use the custom addons, follow these steps:

1. **Log in to your Odoo instance**.
2. **Go to the Apps menu**.
3. **Update the apps list**:
    - Click on the "Update Apps List" button.
4. **Search for the custom modules**:
    - Look for the modules provided in this repository.
5. **Install the desired modules**:
    - Click on the "Install" button next to the module you want to install.

## 📦 Modules

This repository contains the following custom modules:

1. **Module 1**: Description of module 1.
2. **Module 2**: Description of module 2.
3. **Module 3**: Description of module 3.

*(Provide a brief description of each module included in the repository.)*

## 🤝 Contributing

Contributions are welcome! To contribute, follow these steps:

1. **Fork the repository**.
2. **Create a new branch**:
    ```bash
    git checkout -b feature-branch
    ```
3. **Make your changes**.
4. **Commit your changes**:
    ```bash
    git commit -m "Add some feature"
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

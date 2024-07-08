# 🌊 Blue Theme for Odoo

Welcome to the **Blue Theme for Odoo**! This theme provides a sleek and modern look for your Odoo instance with beautiful blue tones and custom logos.

## 📋 Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## 🌟 Overview

The **Blue Theme** enhances your Odoo experience with a fresh and professional look. It includes:
- A blue color scheme for various UI elements.
- Custom logos and favicons.
- Additional styles for forms, buttons, and more.

## ⚙️ Installation

To install the Blue Theme, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/jmillanstem/odoo17-addons.git
    cd odoo17-addons
    ```

2. **Copy the theme to your Odoo addons directory**:
    ```bash
    cp -r blue_theme /path/to/your/odoo/addons/
    ```

3. **Update your Odoo configuration**:
    Add the path to your addons directory in the `odoo.conf` file:
    ```ini
    [options]
    addons_path = /path/to/your/odoo/addons,/path/to/odoo17-addons/blue_theme
    ```

4. **Restart Odoo**:
    ```bash
    sudo systemctl restart odoo
    ```

5. **Update Apps List**:
    - Go to `Apps` in Odoo.
    - Click on `Update Apps List`.
    - Search for `Blue Theme`.
    - Click on `Install`.

## 🚀 Usage

Once installed, the theme will automatically apply to your Odoo instance. You can customize further by modifying the SCSS files in the `static/src/css` directory.

## 🎨 Customization

To customize the theme:
1. **Edit the SCSS file**:
    - Open `static/src/css/style.scss`.
    - Make your changes.
2. **Rebuild the assets**:
    ```bash
    docker-compose exec web odoo -u blue_theme -d your_database_name --stop-after-init
    ```
3. **Restart Odoo**:
    ```bash
    docker-compose restart web
    ```

## 📸 Screenshots

Here are some screenshots of the Blue Theme in action:

![Dashboard](https://via.placeholder.com/800x400?text=Dashboard+with+Blue+Theme)
*Figure 1: Dashboard with Blue Theme*

![Invoices](https://via.placeholder.com/800x400?text=Invoices+with+Blue+Theme)
*Figure 2: Invoices with Blue Theme*

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

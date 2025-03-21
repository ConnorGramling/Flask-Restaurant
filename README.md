# Restaurant Menu & Ordering System

This project is a web-based restaurant menu and ordering system built with Flask and deployed on PythonAnywhere. Designed for mobile access via QR codes placed at each table, the application allows customers to browse the menu, place orders, and notifies both the kitchen and wait staff with order details in real time.

## Features

- **Interactive Digital Menu**  
  Customers scan a table-specific QR code to access the menu, select their items, enter their name, and place an order.

- **Real-Time Kitchen Dashboard**  
  The kitchen staff can view incoming orders along with customer names and table numbers. Orders are updated live and can be marked as completed.

- **Persistent Order Storage**  
  Orders are saved in a server-side database for reliable tracking and display.

- **Table-Specific Ordering**  
  Each order is associated with the table number from which it originated, streamlining service and delivery.

- **Responsive Design**  
  Optimized for all screen sizes including smartphones, with dynamic layout changes based on orientation.

## Live Application

- 🪑 **To place an order (Table 1)**: [https://connorgramling.pythonanywhere.com/table/1](https://connorgramling.pythonanywhere.com/table/1)  
- 👨‍🍳 **To access the kitchen dashboard**: [https://connorgramling.pythonanywhere.com/kitchen/](https://connorgramling.pythonanywhere.com/kitchen/)

## Technologies Used

- Python & Flask  
- HTML / CSS / JavaScript  
- SQLAlchemy (for database models)  
- PythonAnywhere (for deployment)

---

For best experience, access the links on your smartphone to simulate the intended QR code interaction.

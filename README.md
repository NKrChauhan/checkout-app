## Checkout App

This document provides instructions for setting up and running the Checkout App, a Python application that calculates the total price for a shopping cart based on individual and bulk pricing offers.

**Prerequisites:**

- Docker: [https://www.docker.com/](https://www.docker.com/)

**Project Structure:**

```
checkout-app/
├── cart/
│   └── cart.py                        # Contains the Cart class representing a shopping cart
│   └── cart_item.py                   # Contains the CartItem class representing a cart item in a Cart class.
├── checkout/
|   └── helpers                        # Directory containing helpers to help in chekout process 
|       └── regional_tax_rule.py       # Manages tax rules based on region, enabling dynamic tax calculations while checkout. 
│   └── checkout.py                    # Contains the Checkout class responsible for price calculations
│   └── constants.py                   # Contains the constants/enum class
├── Dockerfile                         # Dockerfile for building the image
├── main.py                            # Entrypoint script for running the application
├── product/
│   └── product.py                     # Contains the Product class representing a product with its price and bulk offers
├── requirements.txt                   # File specifying project dependencies
└── tests/                             # Directory for unit tests of cart and checkout
```

##Running the Application:

**Build and Run the Docker Image:**

```bash
cd checkout-app
./run.sh
```
This builds a Docker image named `checkout-app` that includes all project dependencies only after successful execution of the unit tests.

The script will prompt you for cart items string like `Enter cart items:` and display the calculated total price in next line.

if you get the error:
```bash
   permission denied: ./run.sh
```
Run this command before the execution
```bash
chmod +x run.sh
```
Now try to run the command `./run.sh`

#### Demo:
   ```bash
   Enter cart items: DDD
   45.0
   ```

To exit the application press `Ctrl+C`

**Testing:**

- The project contains unittests that runs during the docker image building process to ensure the error free image creation

**Future Enhancements:**

- Implement database integration to store product information and bulk price offers more persistently.
- Explore web frameworks (e.g., DRF/Flask) to create a web-based user interface for interacting with the Checkout App.
- Consider using a more robust configuration management solution to handle application settings and product data.

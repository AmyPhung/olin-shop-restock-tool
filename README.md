# Stock Market Restocking Tool
This tool was created to make restocking the Stock Market outside Olin's shop quicker and easier while opening the doors to improved automation in the future.

**Important Notes:**
- **The `master_inventory.csv` file needs to be sorted by drawer in order to work properly**
- **Don't change column names without updating code (imprtant names: "Name," "McMaster #")**
- **Don't change csv names without updating code**


## Future Potential Developments:
+ Add functionality to save half-done orders
+ Automatically save order date
+ Add all drawers + document how to update inventory
+ Create pretty interface
+ Create easy pip-install + usage instructions - specify dependencies
+ Use cv + april tags to auto-stock components via photos

## Dependencies
pip install fpdf
pip install pyqrcode
pip install Pillow
pip install pypng

## Usage:
- Navigate to base directory
- Run `main.py`
- Select stuff to restock
- Use buttons on top to navigate through pages
- Select `Create Order` button when done

## How To Update Inventory:
-

## How To Add a new drawer:
- See code (add snapshot here)

## Other Helpful Things
- Bulk QR code generator https://qrexplore.com/generate/
- Bar-Code reader app https://play.google.com/store/apps/details?id=it.pw2.bar_code&hl=en

## Troubleshooting
- permission denied - close open pdf

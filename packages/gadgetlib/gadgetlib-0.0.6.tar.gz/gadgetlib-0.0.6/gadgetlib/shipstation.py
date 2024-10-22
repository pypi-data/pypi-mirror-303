import requests
import logging
from datetime import datetime
from requests.auth import HTTPBasicAuth
from typing import List

logger = logging.getLogger(__name__)

class Address:
    def __init__(self, attn, street1, city, state, postal_code, company="", street2="", street3="", country="US", phone=""):
        self.attn = attn
        self.company = company
        self.street1 = street1
        self.street2 = street2
        self.street3 = street3
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.phone = phone
        # self.residential = None #dunno if ill ever use this...
        self.address_verified = "" # Readonly from SS

    def to_dict(self) -> dict:
        output = {
            'name': self.attn,
            'company': self.company,
            'street1': self.street1,
            'street2': self.street2,
            'street3': self.street3,
            'city': self.city,
            'state': self.state,
            'postalCode': self.postal_code,
            'country': self.country,
            'phone': self.phone
        }
        return output

class OrderItem:
    def __init__(self, sku="", name="", quantity=1, unit_price=0):
        self.sku = sku
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price
    
    def to_dict(self) -> dict:
        "Translate the properties of this class into a dict ready to be sent to ShipStation"
        output = {
            'sku': self.sku,
            'name': self.name,
            'quantity': self.quantity,
            'unitPrice': self.unit_price
        }
        return output



class Order:
    """An object which can be passed to a ShipStation object to create an order."""
    def __init__(self, order_number:str, address:Address, date=datetime.today().strftime('%Y-%m-%d'), items:List[OrderItem]=[], email="", customer_notes="", internal_notes="", weight=0):
        self.order_id = "" # ReadOnly from SS
        self.order_number = order_number # Displayed Name
        self.order_key = order_number # Unique internal ID for referencing an order
        self.order_date = date
        self.create_date = "" # Timestamp order was created in SS
        self.modify_date = ""
        self.order_status = "awaiting_shipment"
        self.bill_to = address
        self.ship_to = address
        self.items = items
        self.customer_notes = customer_notes
        self.internal_notes = internal_notes
        self.weight = weight
        self.email = email

    def to_dict(self):
        "Translate the properties of this class into a dict ready to be sent to ShipStation"
        output = {
            'orderNumber': self.order_number,
            'orderDate': self.order_date,
            'orderStatus': self.order_status,
            'customerEmail': self.email,
            'billTo': self.bill_to.to_dict(),
            'shipTo': self.ship_to.to_dict(),
            'items': [item.to_dict() for item in self.items],
            'customerNotes': self.customer_notes,
            'internalNotes': self.internal_notes,
            'weight': {
                'units': "pounds",
                'value': self.weight
            },
            'advancedOptions': {}
        }
        return output



class ShipStation:
    def __init__(self, ss_key: str, ss_secret: str, store_id: str):
        self.store_id = store_id
        self.auth = HTTPBasicAuth(ss_key, ss_secret)
        self.url = "https://ssapi.shipstation.com"

    def get_orders_by_date_range(self, start_date: str, end_date: str, exclude_voided=True):
        """Fetches orders from shipstation & returns them in a dictionary formatted dict[order_id][Inbound/Outbound] = Dict{List[str], Cost:int}

        May result in an exception"""
        page = 1
        today = datetime.today().strftime('%Y-%m-%d')
        output = {}
        params = {
            'storeID': self.store_id,
            'shipDateStart': start_date,
            'shipDateEnd': end_date,
            'page': page
        }

        while True:
            response = requests.get(self.url + "/shipments", auth=self.auth, params=params)
            # guard clause; filters errored requests
            if response.status_code != 200:
                logger.error(f"Failed to retrieve shipments on page {page}: {response.status_code}: {response.text}")
                raise Exception()
            data = response.json()

            # grabs all the tracking #'s associated with each order number and puts them in the 'output' dict
            for shipment in data['shipments']:
                logger.debug(f"Found shipment: {shipment}")
                order_id = shipment.get('orderNumber')
                is_return = shipment.get('isReturnLabel')
                is_voided = shipment.get('voided')
                tracking_number = shipment.get('trackingNumber')

                if is_voided and exclude_voided:
                    continue

                if order_id not in output.keys():
                    output[order_id] = {
                        'Outbound': [],
                        'Inbound': [],
                    }

                if is_return:
                    output[order_id]["Inbound"].append(tracking_number)
                else:
                    output[order_id]["Outbound"].append(tracking_number)
                    
            if data['pages'] and page < data['pages']:
                page += 1
            else:
                break
        
        return output

    def get_todays_shipments(self) -> dict:
        """Fetches orders from shipstation & returns them in a dictionary formatted dict[order_id][Inbound/Outbound] = List[str]

        May result in an exception"""

        today = datetime.today().strftime('%Y-%m-%d')
        return self.get_orders_by_date_range(today, today)
        
    def create_orders(self, orders: List[Order]):
        """Takes a list of order objects & creates them in shipstation. May raise an exception."""
        formatted_orders = []
        create_orders_url = self.url + "/orders/createorders"
        for o in orders:
            o_dict = o.to_dict()
            o_dict["advancedOptions"]["storeId"] = self.store_id
            formatted_orders.append(o_dict)
        
        headers = {
            'Content-Type': 'application/json'
        }

        try:
            response = requests.post(create_orders_url, auth=self.auth, json=formatted_orders, headers=headers)
            if not response.ok:
                logger.error(f"Shipstation returned code {response.status_code} {response.text}\nRelated Orders{formatted_orders}")
                raise Exception("Could not create shipstation orders")
        except Exception as e:
            logger.error(e)
            raise e

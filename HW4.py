# SI 206 HW4
# Your name:
# Your student id:
# Your email:
# Who you worked with on this homework:

import unittest

class Customer:
    def __init__(self, name, cust_id, wallet = 10):
        '''initializes the name, customer ID, and the amount of money on the customer's wallet'''
        self.name = name
        self.cust_id = cust_id
        self.wallet = wallet

    def __str__(self):
        '''returns the name of the customer and their customer ID'''
        return f'My name is {self.name}, and my customer ID is {self.cust_id}'

    def reload_wallet(self, amount):
        '''reloads the customers wallet with the passed amount'''
        self.wallet += amount

    def place_order(self, vendor, order):
        ''' 
        1) Call the calculate_cost method to calculate the total cost of the 
           order by totaling the cost for each produce object in the order.
        2) Check if the customer has the total cost or more in their wallet.
           If they do not have enough money then print "Insufficient funds"
           and return False.
        3) Call the process_order method on the vendor object. If process_order
           returns True remove the total cost from the customer’s wallet and
           add it to the vendor's earnings and return True.
           Otherwise, return False.
        '''

        pass
 
class Produce:

    def __init__(self, name, cost):
        ''' initializes the name and cost'''
        self.name = name
        self.cost = cost

    def __str__(self):
        ''' returns the name and cost'''
        return self.name + " " + str(self.cost)

class Vendor:

    def __init__(self, name, earnings=0):
        ''' 
        initializes the name and earnings of the vendor
        sets the inventory to an empty dictionary
        '''
        self.name = name
        self.earnings = earnings
        self.inventory = {}
    
    def __str__(self):
        '''returns the name of the vendor and their inventory'''
        print(f"Hello we are {self.name}. This is the current inventory {self.inventory.keys()}")

    def receive_payment(self, amount):
        '''adds the passed amount to the vendors earnings'''
        self.earnings += amount

    def calculate_cost(self, produce, quantity, fresh_pick, customer):
        '''
        takes the produce object, quantity, and a boolean variable fresh_pick, 
        which specifics whether the order requests for fresh pick or a regular pick. 
        If a fresh pick is requested, it adds $1.50 to the per pound cost

        EXTRA CREDIT: It also checks for every customer whose ID is a multiple of 100 
        (cust_id=100, 200, 300 etc) and gives them a 15% discount on every item
        '''
        pass

    def stock_up(self, produce, quantity):
        ''' 
        If the produce is already in the inventory then add the passed quantity
        to the existing value.  Otherwise set the value for the produce
        in the inventory dictionary.
        '''
        pass

    def process_order(self, order):
        '''
        Checks that there is enough produce for an order and if not returns False,
        otherwise it subtracts the produce item from the quantity in the inventory
        and returns True.
        '''
    
        pass


class TestAllMethods(unittest.TestCase):

    def setUp(self):
        self.tomatoes = Produce('Tomatoes',3.00)
        self.potatoes = Produce('Potatoes', 1.75)
        self.onions = Produce('Onions', 1.50)
        self.bananas = Produce('Bananas', 0.75)

        self.bob = Customer(name='Bob', cust_id=100)
        self.alice = Customer(name='Alice', cust_id=25, wallet=1.50)

        self.clydes_fruits = Vendor(name="Clyde's Fruits")
        self.rebeccas_home_garden = Vendor(name="Rebecca's Home Garden")

    # Check the constructors
    def test_customer_constructor(self):
        self.assertEqual(self.bob.name, 'Bob')
        self.assertEqual(self.bob.wallet, 10)

    def test_produce_constructor(self):
        self.assertEqual(self.onions.name, 'Onions')
        self.assertAlmostEqual(self.onions.cost, 1.50, 1)
        self.assertEqual(self.bananas.name, 'Bananas')
        self.assertAlmostEqual(self.bananas.cost, 0.75, 0)

    def test_vendor_constructor(self):
        self.assertEqual(self.clydes_fruits.name, "Clyde's Fruits")
        self.assertEqual(self.clydes_fruits.earnings, 0)
        self.assertEqual(self.rebeccas_home_garden.name,"Rebecca's Home Garden")
        self.assertEqual(self.rebeccas_home_garden.inventory, {})

    # Check the reload_wallet method for customer
    def test_customer_reload_wallet(self):
        self.alice.reload_wallet(10)
        self.assertAlmostEqual(self.alice.wallet, 11.50, 1)

    # Check the calculate_cost for vendor
    def test_vendor_calculate_cost(self):
        self.assertAlmostEqual(self.clydes_fruits.calculate_cost(self.onions, 10, False, self.alice), 15.00, 2)

    # Check if discount is applied
        self.assertAlmostEqual(self.rebeccas_home_garden.calculate_cost(self.tomatoes, 3, False, self.alice), 9, 2)
    
    # Check if fresh picks are billed correctly
        self.assertAlmostEqual(self.rebeccas_home_garden.calculate_cost(self.bananas, 3, True, self.alice), 6.75, 2)

    #EXTRA CREDIT: UNCOMMENT THE TEST BELOW: Check if every customer with an ID that is a multiple of a 100 gets the discount
        # self.assertAlmostEqual(self.rebeccas_home_garden.calculate_cost(self.tomatoes, 3, False, self.bob), 7.65, 2)


    # Check the receive_payment method for vendor
    def test_vendor_receive_payment(self):
        self.rebeccas_home_garden.receive_payment(50)
        self.assertAlmostEqual(self.rebeccas_home_garden.earnings, 50.00, 0)

    # Check the stock_up method for vendor
    def test_vendor_stock_up(self):
        self.rebeccas_home_garden.stock_up(self.tomatoes, 4)
        self.rebeccas_home_garden.stock_up(self.potatoes, 10)
        self.assertEqual(self.rebeccas_home_garden.inventory, {self.tomatoes: 4, self.potatoes: 10})

        self.clydes_fruits.stock_up(self.onions, 5)
        self.clydes_fruits.stock_up(self.bananas, 3)
        self.assertEqual(self.clydes_fruits.inventory, {self.onions: 5, self.bananas: 3})

    # Check the place_order method for customer
    def test_customer_place_order(self):
        ted = Customer(name='Ted', cust_id=50)
        franks_fresh_finds = Vendor(name="Frank's Fresh Finds")

        franks_fresh_finds.stock_up(self.bananas, 5)
        franks_fresh_finds.stock_up(self.tomatoes, 3)

        # Scenario 1: customer doesn't have enough money in their wallet
        
    
		# Scenario 2: vendor doesn't have enough produce left in stock
        

        # Scenario 3: vendor doesn't sell that produce item
        
   
    def test_customer_place_order_2(self):
        ali = Customer(name='Ali', cust_id=200)
        randys_ranch = Vendor(name="Randy's Ranch")
        randys_ranch.stock_up(self.onions, 5)
        randys_ranch.stock_up(self.potatoes, 10)

        # Fix the test cases below to check if the customer's wallet and the vendor's earnings has 
        # the right amount after an order is processed
        
        self.assertEqual(ali.place_order(randys_ranch, {self.onions: {"quantity": 2,"fresh_pick": False}, self.potatoes: {"quantity": 4,"fresh_pick": False}}), False)
        self.assertAlmostEqual(self.ali.wallet, 1.50, 0)
        self.assertAlmostEqual(ali.earnings, 8.50, 0)
    

def main():
    pass

if __name__ == '__main__':
    unittest.main(verbosity = 2)
    main()

{
    'name': 'Hotel Management System',
    'version': '1.0',
    'category': 'Hotel Management',
    'summary': 'Manage hotel floors, rooms, customers, and bookings.',
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'depends': ['base'],
    'data': [
    'security/groups.xml',  # Ensure this file is included
    'security/ir.model.access.csv',  # Ensure this file is included
    'views/hotel_booking_views.xml',
    'views/hotel_customer_views.xml',
    'views/hotel_floor_views.xml',
    'views/hotel_room_views.xml',
    'views/hotel_employee_views.xml',
    'data/hotel_employees.xml'
    ]
}

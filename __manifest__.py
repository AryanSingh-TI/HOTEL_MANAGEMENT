{
    'name': 'Hotel Management System',
    'version': '1.0',
    'category': 'Hotel Management',
    'summary': 'Manage hotel floors, rooms, customers, and bookings.',
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'depends': ['base'],
    'data': [
    'security/groups.xml', 
    'security/ir.model.access.csv',
    'views/hotel_booking_views.xml',
    'views/hotel_customer_views.xml',
    'views/hotel_floor_views.xml',
    'views/hotel_room_views.xml',
    'views/hotel_employee_views.xml',
    'views/hotel_todo_views.xml',
    'views/hotel_customer_booking.xml',
    'views/hotel_rating_customer.xml',
    'views/hotel_rating_admin.xml',
    'views/hotel_attendance_employee.xml',
    'views/hotel_attendance_admin.xml',
    'data/hotel_employees.xml'
    ] ,
    'assets': {
    'web.assets_backend': [
        'HOTEL_MANAGEMENT/static/src/css/styles.css',
    ],
},
}

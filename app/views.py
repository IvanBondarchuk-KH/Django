from django.http import HttpResponse

menu = """
<a href="/">Home</a> |
<a href="/about/">About Us</a> |
<a href="/contacts/">Contacts</a> |
<a href="/products/">Our Products</a> |
<a href="/students/">Students</a> |
<a href="/profile/">User Profile</a> |
<a href="/sales/">Sales</a>
"""

def home(request):
    return HttpResponse(f"""
        <h1>Home</h1>
        <p>Welcome to our website!</p>
        {menu}
    """)

def about(request):
    return HttpResponse(f"""
        <h1>About Us</h1>
        <p>We are learning Django!</p>
        {menu}
    """)

def contacts(request):
    return HttpResponse(f"""
        <h1>Contacts</h1>
        <p>Contact us at: email@example.com</p>
        {menu}
    """)

def products(request):
    return HttpResponse(f"""
        <h1>Our Products</h1>
        <ul>
            <li>Apple MacBook Pro 16" Laptop M5 Max 48GB/2TB 2026 Space Black - 298 999 UAH</li>
            <li>Logitech PRO X 2 SUPERLIGHT 2 LIGHTSPEED 8000Hz Gaming Mouse - 17 759 UAH</li>
            <li>Black RGB Backlit Tenkeyless (TKL) Optical Gaming Keyboard with OmniPoint 2.0 Switches and OLED Display - 42 366 UAH</li>
        </ul>
        {menu}
    """)

def students(request):
    return HttpResponse(f"""
        <h1>Students</h1>
        <table border="1">
            <tr><th>Name</th><th>Age</th><th>Course</th></tr>
            <tr><td>Ivan</td><td>12</td><td>Django</td></tr>
            <tr><td>Artem</td><td>8</td><td>Python</td></tr>
        </table>
        {menu}
    """)

def profile(request):
    name = "Ivan"
    age = 12
    city = "Kharkiv"
    return HttpResponse(f"""
        <h1>User Profile</h1>
        <p>Name: {name}</p>
        <p>Age: {age}</p>
        <p>City: {city}</p>
        {menu}
    """)

def sales(request):
    return HttpResponse(f"""
        <style>
            body {{ background: lightblue; }}
        </style>
        <h1>Sales</h1>
        <p>Here you will find our promotions and discounts!</p>
        {menu}
    """)
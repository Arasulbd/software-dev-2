from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

# Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/blogDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

db = SQLAlchemy(app)

from flask_migrate import Migrate
migrate = Migrate(app, db)
# Models

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    cart_items = db.relationship('CartItem', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    product_desc = db.Column(db.String(100), nullable=True)
    image_url = db.Column(db.Text, nullable=True)
    product_price = db.Column(db.Float, nullable=False)

  
class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1, nullable=False)
    product = db.relationship('Product')


with app.app_context():

    db.create_all()
    if Product.query.count() == 0:
        sample_products = [
            Product(product_name='Shirts', product_desc="This is a Shirt", image_url=" ", product_price=200),
            Product(product_name='Trousers', product_desc="This is a Trouser", image_url=" ", product_price=200),
            Product(product_name='Off Outfit', product_desc="This is an Off Outfit", image_url=" ", product_price=200),
            Product(product_name="Men's Casual Fashion Coat", product_desc="This is a Fashion Coat", image_url=" ", product_price=200),
        ]
        db.session.bulk_save_objects(sample_products)
        db.session.commit()

# Routes

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/base')
def base():
    products = Product.query.all()
    return render_template('base.html', products=products)

@app.route('/check_out', methods=['POST', 'GET'])
def check_out():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        
        card = request.form['card']
        expiry = request.form['expiry']
        cvv = request.form['cvv']
        if not all([name, email, address, card, expiry, cvv]):
            flash('Please fill in all required fields.')
            return redirect(url_for('check_out'))
        flash('Order placed successfully! Thank you for shopping with us.')
        session.pop('cart', None)  # clear the cart after successful checkout
        return redirect(url_for('index'))
      
    return render_template('check_out.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            flash('Username already exists.')
            return redirect(url_for('register'))
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. Please login.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.check_password(request.form['password']):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Login successful.')
            return redirect(url_for('index'))
        flash('Invalid credentials.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out.')
    return redirect(url_for('index'))

'''
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.form.get('product_id')

    if not product_id:
        flash('Invalid product ID')
        return redirect(url_for('index'))

    product_id = str(product_id)  

    cart = session.get('cart', {})

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    session['cart'] = cart
    flash('Product added to cart')
    return redirect(url_for('index'))

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.form.get('product_id')
    action = request.form.get('action')  # Get the action from the form

    if not product_id:
        flash('Invalid product ID')
        return redirect(url_for('cart'))

    product_id = str(product_id)
    cart = session.get('cart', {})

    if action == 'increment':
        cart[product_id] = cart.get(product_id, 0) + 1

    elif action == 'decrement':
        if product_id in cart:
            cart[product_id] -= 1
            if cart[product_id] <= 0:
                del cart[product_id]

    elif action == 'remove':
        cart.pop(product_id, None)

    else:
        # Default to increment if no action is provided
        cart[product_id] = cart.get(product_id, 0) + 1

    session['cart'] = cart
    flash(f'Cart updated: {action}')
    return redirect(url_for('cart'))
'''
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.form.get('product_id')
    action = request.form.get('action')

    if not product_id:
        flash('Invalid product ID')
        return redirect(request.referrer or url_for('index'))

    product_id = str(product_id)
    cart = session.get('cart', {})

    if action == 'increment':
        cart[product_id] = cart.get(product_id, 0) + 1
    elif action == 'decrement':
        if product_id in cart:
            cart[product_id] -= 1
            if cart[product_id] <= 0:
                del cart[product_id]
    elif action == 'remove':
        cart.pop(product_id, None)
    else:
        cart[product_id] = cart.get(product_id, 0) + 1

    session['cart'] = cart
    flash('Cart updated')
    return redirect(request.referrer or url_for('index'))  



@app.route('/cart')
def cart():
    cart = session.get('cart', {})
    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        product = Product.query.get(int(product_id)) 
        if product:
            subtotal = product.product_price * quantity
            total += subtotal
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal
            })

    return render_template('cart.html', cart_items=cart_items, total=total) 



   
if __name__ == '__main__':
    app.run(debug=True, port=8000)

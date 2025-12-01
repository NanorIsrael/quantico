import { Menu, X, Phone, Mail, MapPin, Clock, Star, Award, Users, ChefHat } from 'lucide-react';
import bruschetta from "../assets/images/menu/Bruschetta.jpg";


function MenuPage() {
  const menuCategories = [
    {
      category: 'Starters',
      items: [
        { name: 'Bruschetta', description: 'Fresh tomatoes, basil, olive oil, and toasted baguette', price: '$8.50', image:"../assets/images/menu/Bruschetta.jpg" },
        // { name: 'French Onion Soup', description: 'Classic soup with caramelized onions and gruyere cheese', price: '₵38' },
        { name: 'Caesar Salad', description: 'Fresh mozzarella, tomatoes, basil, and balsamic glaze', price: '₵42' },
        // { name: 'Escargots de Bourgogne', description: 'Burgundy snails in garlic herb butter', price: '₵55' }
      ]
    },
    {
      category: 'Main Courses',
      items: [
        { name: 'Grilled Salmon', description: 'Atlantic salmon with lemon butter sauce and seasonal vegetables', price: '₵120' },
        { name: 'Beef Tenderloin', description: 'Prime beef with red wine reduction and truffle mashed potatoes', price: '₵145' },
        { name: 'Chicken Cordon Bleu', description: 'Stuffed chicken breast with ham and swiss cheese', price: '₵95' },
        { name: 'Vegetarian Risotto', description: 'Creamy arborio rice with seasonal vegetables and parmesan', price: '₵85' },
        { name: 'Lamb Chops', description: 'Herb-crusted lamb with rosemary jus and roasted vegetables', price: '₵135' },
        { name: 'Seafood Linguine', description: 'Fresh seafood in white wine garlic sauce', price: '₵110' }
      ]
    },
    {
      category: 'Desserts',
      items: [
        { name: 'Crème Brûlée', description: 'Classic French custard with caramelized sugar', price: '₵35' },
        { name: 'Chocolate Lava Cake', description: 'Warm chocolate cake with vanilla ice cream', price: '₵40' },
        { name: 'Tiramisu', description: 'Italian coffee-flavored dessert with mascarpone', price: '₵38' },
        { name: 'Fruit Tart', description: 'Fresh seasonal fruits on vanilla custard', price: '₵32' }
      ]
    },
    {
      category: 'Beverages',
      items: [
        { name: 'House Wine (Glass)', description: 'Red or White selection', price: '₵35' },
        { name: 'Premium Cocktails', description: 'Chef\'s signature cocktails', price: '₵45' },
        { name: 'Fresh Juices', description: 'Orange, Apple, Pineapple, or Mixed', price: '₵20' },
        { name: 'Specialty Coffee', description: 'Espresso, Cappuccino, or Latte', price: '₵25' }
      ]
    }
  ];

  return (
    <div className="py-16">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <h1 className="text-5xl font-serif font-bold text-stone-900 mb-4">Our Menu</h1>
          <p className="text-lg text-stone-600">Crafted with passion, served with excellence</p>
        </div>

        <div className="space-y-12">
          {menuCategories.map((category, idx) => (
            <div key={idx} className="bg-white rounded-lg shadow-lg p-8">
              <h2 className="text-3xl font-serif font-bold text-amber-600 mb-6 pb-3 border-b-2 border-amber-200">
                {category.category}
              </h2>
              <div className="grid gap-6">
                {category.items.map((item, itemIdx) => (
                  <div key={itemIdx} className="flex justify-between items-start gap-2">
                    <figure className='relative w-[200px] h-[200px]'>
                      <img src={bruschetta} alt={'previewing bruschetta'} className= 'object-cover rounded-sm'/>
                    </figure>
                    <div className="flex-1">
                      <h3 className="text-xl font-semibold text-stone-900 mb-1">{item.name}</h3>
                      <p className="text-stone-600">{item.description}</p>
                    </div>
                    <div className="ml-4 text-xl font-bold text-amber-600">{item.price}</div>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>

        <div className="mt-12 bg-amber-50 border-l-4 border-amber-600 p-6 rounded-lg">
          <p className="text-stone-700">
            <strong>Note:</strong> Menu items and prices are subject to change based on seasonal availability. 
            Please inform our staff of any dietary restrictions or allergies.
          </p>
        </div>
      </div>
    </div>
  );
}
export default MenuPage;
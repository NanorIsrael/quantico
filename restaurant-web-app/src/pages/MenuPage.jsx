import bruschetta from "../assets/images/menu/Bruschetta.jpg";
import saladCeasar from "../assets/images/menu/salad-recipe.jpg";
import grilledSalmon from "../assets/images/menu/grilled-salmon.jpg";
import ribEyeStreak from "../assets/images/menu/RibEye-Streak.jpg";
import vegetableRisotto from "../assets/images/menu/vegetable-risotto.jpeg";
import tiramisuRecipe from "../assets/images/menu/Tiramisu-Recipe.jpg";
import berrycheesecake from "../assets/images/menu/Berrycheesecake.jpg";
import redWine from "../assets/images/menu/redwines.jpeg";
import whiteWine from "../assets/images/menu/whitewine.avif";
import craftBeer from "../assets/images/menu/craftbeer.jpg";
import nespresso from "../assets/images/menu/nespresso.avif";


function MenuPage() {
  const images= [
    bruschetta, saladCeasar, grilledSalmon, ribEyeStreak, vegetableRisotto,
     tiramisuRecipe, berrycheesecake, redWine, whiteWine, craftBeer, nespresso
  ]
  const menuCategories = [
    {
      category: 'Starters',
      items: [
        { name: 'Bruschetta', description: 'Fresh tomatoes, basil, olive oil, and toasted baguette', price: '$8.50', image: 0 },
        // { name: 'French Onion Soup', description: 'Classic soup with caramelized onions and gruyere cheese', price: '₵38' },
        { name: 'Caesar Salad', description: 'Crisp romaine with homemade Caesar dressing:', price: '$9.00', image: 1},
        // { name: 'Escargots de Bourgogne', description: 'Burgundy snails in garlic herb butter', price: '₵55' }
      ]
    },
    {
      category: 'Main Courses',
      items: [
        { name: 'Grilled Salmon', description: ' Served with lemon butter sauce and seasonal vegetables', price: '$22.00', image: 2 },
        { name: 'Ribeye Steak', description: '12 oz prime cut with garlic mashed potatoes', price: '$28.00', image: 3 },
        // { name: 'Chicken Cordon Bleu', description: 'Stuffed chicken breast with ham and swiss cheese', price: '₵95' },
        { name: 'Vegetarian Risotto', description: 'Creamy arborio rice with wild mushrooms', price: '₵85', image: 4},
        // { name: 'Lamb Chops', description: 'Herb-crusted lamb with rosemary jus and roasted vegetables', price: '₵135' },
        // { name: 'Seafood Linguine', description: 'Fresh seafood in white wine garlic sauce', price: '₵110' }
      ]
    },
    {
      category: 'Desserts',
      items: [
        // { name: 'Crème Brûlée', description: 'Classic French custard with caramelized sugar', price: '₵35' },
        { name: 'Cheesecake', description: 'Creamy cheesecake with berry compote', price: '$7.00',  image: 6 },
        { name: 'Tiramisu', description: 'Classic Italian dessert with mascarpone', price: '$7.50',  image: 5},
        // { name: 'Fruit Tart', description: 'Fresh seasonal fruits on vanilla custard', price: '₵32' }
      ]
    },
    {
      category: 'Beverages',
      items: [
        { name: 'Red Wine (Glass)', description: 'A selection of Italian reds', price: '$10.00', image: 7 },
        { name: 'White Wine (Glass)', description: 'Crisp and refreshing', price: '$9.00', image: 8 },
        { name: 'Craft Beer', description: 'Local artisan brews', price: '$6.00', image: 9 },
        { name: 'Espresso', description: 'Strong and aromatic', price: '$3.00', image: 10 }
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
                    <figure className='relative w-[200px] h-[120px]'>
                      <img src={images[item.image]} alt={'previewing bruschetta'} className= 'absolute inset-0 object-cover rounded-sm w-full h-full'/>
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
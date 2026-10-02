import Link from 'next/link';
import siteData from '@/data/site.json';

export default function Footer() {
  return (
    <footer className="bg-navy-900 text-white pt-16 pb-8">
      <div className="container mx-auto px-4 grid grid-cols-1 md:grid-cols-4 gap-8">
        <div>
          <h3 className="text-xl font-bold mb-4">{siteData.store.name}</h3>
          <p className="text-gray-400 mb-4">{siteData.store.shortStory}</p>
          <div className="text-gray-400">
            <p>{siteData.store.address}</p>
            <p>Phone: {siteData.store.phone}</p>
            <p>Email: {siteData.store.email}</p>
          </div>
        </div>
        <div>
          <h4 className="font-bold mb-4">Shop</h4>
          <ul className="space-y-2 text-gray-400">
            {siteData.categories.slice(0, 5).map(c => (
              <li key={c.slug}><Link href={`/collections/${c.slug}`} className="hover:text-white">{c.name}</Link></li>
            ))}
          </ul>
        </div>
        <div>
          <h4 className="font-bold mb-4">Information</h4>
          <ul className="space-y-2 text-gray-400">
            <li><Link href="/about" className="hover:text-white">About Us</Link></li>
            <li><Link href="/contact" className="hover:text-white">Contact Us</Link></li>
            <li><Link href="/bulk-orders" className="hover:text-white">Bulk Orders</Link></li>
          </ul>
        </div>
        <div>
          <h4 className="font-bold mb-4">Policies</h4>
          <ul className="space-y-2 text-gray-400">
            <li><Link href="#" className="hover:text-white">Shipping Policy</Link></li>
            <li><Link href="#" className="hover:text-white">Return Policy</Link></li>
            <li><Link href="#" className="hover:text-white">Privacy Policy</Link></li>
            <li><Link href="#" className="hover:text-white">Terms of Service</Link></li>
          </ul>
        </div>
      </div>
      <div className="container mx-auto px-4 mt-12 pt-8 border-t border-gray-700 text-center text-gray-400">
        <p>&copy; {new Date().getFullYear()} {siteData.store.name}. All rights reserved.</p>
      </div>
    </footer>
  );
}
import os

base_dir = "/Users/samakshsingh/Documents/demo sports site"

header_content = """
'use client';
import Link from 'next/link';
import { useState } from 'react';
import { useCart } from '@/lib/CartContext';
import siteData from '@/data/site.json';
import { useRouter } from 'next/navigation';

export default function Header() {
  const { items, setIsCartOpen } = useCart();
  const [search, setSearch] = useState('');
  const router = useRouter();

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (search.trim()) {
      router.push(`/search?q=${encodeURIComponent(search)}`);
    }
  };

  return (
    <header className="w-full font-sans">
      {/* Top Black Bar */}
      <div className="bg-[#111111] text-white text-[11px] font-medium py-2 px-6 flex justify-between items-center tracking-widest uppercase">
        <div className="hidden md:block">
          {siteData.announcement}
        </div>
        <div className="flex items-center space-x-6 ml-auto">
          <span className="cursor-pointer flex items-center">
            INR
            <svg className="w-3 h-3 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 9l-7 7-7-7"></path></svg>
          </span>
          <Link href="#" className="flex items-center hover:text-gray-300">
            <svg className="w-4 h-4 mr-1.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="1.5" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
            Login
          </Link>
          <button className="flex items-center hover:text-gray-300" onClick={() => setIsCartOpen(true)}>
            <svg className="w-4 h-4 mr-1.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="1.5" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"></path></svg>
            {items.reduce((a, b) => a + b.quantity, 0)}
          </button>
        </div>
      </div>
      
      {/* Main White Header */}
      <div className="bg-white px-6 py-5 flex items-center justify-between border-b border-gray-200">
        {/* Logo */}
        <div className="flex-shrink-0 w-1/4">
          <Link href="/" className="inline-flex flex-col text-black">
            <span className="text-2xl font-serif tracking-[0.15em] uppercase leading-none">Patiala</span>
            <span className="text-[9px] font-sans tracking-[0.3em] uppercase mt-1">Sports House</span>
          </Link>
        </div>
        
        {/* Center Menu */}
        <nav className="hidden lg:flex flex-1 justify-center space-x-7 text-[12px] font-medium text-black">
          {siteData.categories.slice(0, 6).map(cat => (
            <div key={cat.slug} className="group relative cursor-pointer">
              <Link href={`/collections/${cat.slug}`} className="flex items-center hover:text-gray-600">
                {cat.name.replace(' and ', ' & ')}
                <svg className="w-3 h-3 ml-1 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 9l-7 7-7-7"></path></svg>
              </Link>
            </div>
          ))}
          <div className="relative group cursor-pointer">
             <span className="flex items-center hover:text-gray-600">
               More
               <svg className="w-3 h-3 ml-1 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 9l-7 7-7-7"></path></svg>
             </span>
             <div className="absolute top-full left-0 pt-4 hidden group-hover:block z-50">
               <div className="bg-white shadow-lg border border-gray-100 min-w-[150px] py-2">
                 {siteData.categories.slice(6).map(cat => (
                   <Link key={cat.slug} href={`/collections/${cat.slug}`} className="block px-4 py-2 text-[12px] hover:bg-gray-50 text-black">
                     {cat.name}
                   </Link>
                 ))}
               </div>
             </div>
          </div>
        </nav>

        {/* Right Search */}
        <div className="flex-shrink-0 w-1/4 flex justify-end">
          <form onSubmit={handleSearch} className="relative w-full max-w-[220px]">
            <input 
              type="text" 
              placeholder="Search" 
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              className="w-full border border-gray-400 rounded-none pl-3 pr-8 py-1.5 text-[13px] focus:outline-none focus:border-black transition-colors"
            />
            <button type="submit" className="absolute right-2 top-1.5 text-gray-500 hover:text-black">
              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="1.5" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
            </button>
          </form>
        </div>
      </div>
    </header>
  );
}
"""

hero_content = """
import Image from 'next/image';
import Link from 'next/link';
import siteData from '@/data/site.json';
import productsData from '@/data/products.json';
import ProductCard from '@/components/ProductCard';

export default function Home() {
  const bestSellers = productsData.filter(p => p.tags.includes('bestseller')).slice(0, 4);
  
  return (
    <div className="font-sans">
      {/* Hero Section */}
      <section className="relative w-full h-[600px] bg-gray-100 flex flex-col justify-center items-center overflow-hidden">
        <video 
          autoPlay 
          muted 
          loop 
          playsInline 
          poster="/images/hero/hero-video-poster.webp"
          className="absolute inset-0 w-full h-full object-cover"
        >
        </video>
        {/* Subtle overlay so text is readable if there's text, but Devans has no text in center usually. 
            The prompt says "headline, tagline, and buttons". Let's make them elegant and not so brutalist. */}
        <div className="absolute inset-0 bg-black/30 z-10" />
        
        <div className="relative z-20 text-center text-white px-4 flex flex-col items-center mt-12">
          <h1 className="text-4xl md:text-5xl font-serif font-bold mb-4 tracking-wide shadow-sm">{siteData.store.name}</h1>
          <p className="text-lg md:text-xl mb-10 font-light tracking-wider shadow-sm">{siteData.store.tagline}</p>
          
          <div className="flex flex-col sm:flex-row items-center gap-4">
            <Link href="/collections/cricket" className="bg-white text-black font-semibold text-sm py-3 px-10 tracking-widest uppercase hover:bg-gray-100 transition-colors">
              Shop Now
            </Link>
            <a href={`https://wa.me/${siteData.store.phone.replace(/[^0-9]/g, '')}`} target="_blank" rel="noreferrer" className="bg-transparent border border-white text-white font-semibold text-sm py-3 px-10 tracking-widest uppercase hover:bg-white/10 transition-colors">
              WhatsApp Order
            </a>
          </div>
        </div>
      </section>

      {/* Brand Strip (Elegant text only) */}
      <section className="py-6 border-b border-gray-200">
        <div className="container mx-auto px-4 flex justify-center items-center flex-wrap gap-8 md:gap-16">
          {siteData.brands.map((brand, idx) => (
            <div key={idx} className="text-lg font-serif text-gray-500 uppercase tracking-widest">{brand}</div>
          ))}
        </div>
      </section>

      {/* Categories */}
      <section className="py-16 container mx-auto px-6">
        <div className="text-center mb-10">
          <h2 className="text-2xl font-serif font-medium tracking-wide">Shop by Category</h2>
          <div className="w-12 h-[1px] bg-black mx-auto mt-4"></div>
        </div>
        
        <div className="grid grid-cols-2 md:grid-cols-5 gap-6">
          {siteData.categories.slice(0, 5).map(cat => (
            <Link key={cat.slug} href={`/collections/${cat.slug}`} className="group block text-center">
              <div className="relative aspect-[4/5] bg-gray-100 mb-4 overflow-hidden">
                <Image src={`/images/categories/${cat.slug}.webp`} alt={cat.name} fill className="object-cover group-hover:scale-105 transition-transform duration-700" />
              </div>
              <h3 className="text-[13px] font-medium tracking-wider uppercase group-hover:text-gray-500">{cat.name}</h3>
            </Link>
          ))}
        </div>
      </section>

      {/* Best Sellers */}
      <section className="py-16 bg-gray-50">
        <div className="container mx-auto px-6">
          <div className="text-center mb-10">
            <h2 className="text-2xl font-serif font-medium tracking-wide">Featured Products</h2>
            <div className="w-12 h-[1px] bg-black mx-auto mt-4"></div>
          </div>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-x-6 gap-y-10">
            {bestSellers.map(product => (
              <ProductCard key={product.id} product={product} />
            ))}
          </div>
        </div>
      </section>
      
      {/* ... keeping other sections simple and elegant ... */}
    </div>
  );
}
"""

card_content = """
import Link from 'next/link';
import Image from 'next/image';
import { Product } from '@/types';

export default function ProductCard({ product }: { product: Product }) {
  return (
    <Link href={`/products/${product.slug}`} className="group block text-center">
      <div className="bg-gray-100 aspect-[4/5] relative overflow-hidden mb-4">
        <Image 
          src={product.imagePaths[0]} 
          alt={product.name}
          fill
          className="object-cover group-hover:scale-105 transition-transform duration-700"
        />
        {product.tags.includes('new') && (
          <span className="absolute top-2 left-2 bg-black text-white text-[10px] uppercase tracking-widest px-2 py-1">New</span>
        )}
      </div>
      <div className="text-gray-500 text-[11px] mb-1 uppercase tracking-widest">{product.brand}</div>
      <h3 className="text-[13px] font-medium text-gray-900 group-hover:text-gray-500 transition-colors mb-2 line-clamp-1 px-2">{product.name}</h3>
      <div className="flex items-center justify-center space-x-2 text-[13px]">
        <span className="font-medium">Rs. {product.price}</span>
        {product.compareAtPrice && (
          <span className="text-gray-400 line-through">Rs. {product.compareAtPrice}</span>
        )}
      </div>
    </Link>
  );
}
"""

with open(os.path.join(base_dir, "components/Header.tsx"), "w") as f:
    f.write(header_content.strip() + "\\n")
with open(os.path.join(base_dir, "app/page.tsx"), "w") as f:
    f.write(hero_content.strip() + "\\n")
with open(os.path.join(base_dir, "components/ProductCard.tsx"), "w") as f:
    f.write(card_content.strip() + "\\n")

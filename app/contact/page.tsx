"use client";

import siteData from '@/data/site.json';

export default function ContactPage() {
  return (
    <div className="container mx-auto px-4 py-12">
      <div className="max-w-5xl mx-auto">
        <h1 className="text-4xl font-bold mb-12 text-center">Contact Us</h1>
        
        <div className="grid md:grid-cols-2 gap-12">
          <div>
            <h2 className="text-2xl font-bold mb-6">Get in Touch</h2>
            <div className="space-y-6 text-gray-700">
              <div>
                <strong className="block text-black">Visit Our Store:</strong>
                <p>{siteData.store.address}</p>
              </div>
              <div>
                <strong className="block text-black">Call Us:</strong>
                <p>{siteData.store.phone}</p>
              </div>
              <div>
                <strong className="block text-black">Email:</strong>
                <p>{siteData.store.email}</p>
              </div>
              <div>
                <strong className="block text-black">Store Hours:</strong>
                <p>{siteData.store.hours}</p>
              </div>
            </div>
          </div>
          
          <div className="bg-gray-50 p-8 rounded-xl">
            <h2 className="text-2xl font-bold mb-6">Send a Message</h2>
            <form className="space-y-4">
              <div>
                <label className="block text-sm font-medium mb-1">Name</label>
                <input type="text" className="w-full border border-gray-300 rounded p-2 focus:ring-2 focus:ring-orange-500 focus:outline-none" />
              </div>
              <div>
                <label className="block text-sm font-medium mb-1">Email</label>
                <input type="email" className="w-full border border-gray-300 rounded p-2 focus:ring-2 focus:ring-orange-500 focus:outline-none" />
              </div>
              <div>
                <label className="block text-sm font-medium mb-1">Message</label>
                <textarea rows={4} className="w-full border border-gray-300 rounded p-2 focus:ring-2 focus:ring-orange-500 focus:outline-none"></textarea>
              </div>
              <button type="button" onClick={() => alert('UI only')} className="bg-navy-900 text-white font-bold py-2 px-6 rounded hover:bg-black transition-colors">
                Send Message
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}
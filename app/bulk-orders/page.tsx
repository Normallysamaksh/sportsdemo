"use client";

export default function BulkOrdersPage() {
  return (
    <div className="container mx-auto px-4 py-12">
      <div className="max-w-3xl mx-auto text-center">
        <h1 className="text-4xl font-bold mb-6">Bulk & Institutional Orders</h1>
        <p className="text-lg text-gray-600 mb-12">
          We supply schools, colleges, academies, and corporate clubs with high-quality sports equipment and customized uniforms at special institutional rates.
        </p>
      </div>

      <div className="max-w-2xl mx-auto bg-gray-50 p-8 rounded-xl border border-gray-100">
        <h2 className="text-2xl font-bold mb-6">Request a Quote</h2>
        <form className="space-y-4">
          <div className="grid md:grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium mb-1">Contact Name</label>
              <input type="text" className="w-full border border-gray-300 rounded p-2" />
            </div>
            <div>
              <label className="block text-sm font-medium mb-1">Institution/Club Name</label>
              <input type="text" className="w-full border border-gray-300 rounded p-2" />
            </div>
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">Email Address</label>
            <input type="email" className="w-full border border-gray-300 rounded p-2" />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">Phone Number</label>
            <input type="tel" className="w-full border border-gray-300 rounded p-2" />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">Requirements (Please specify products, quantities, and if customization is needed)</label>
            <textarea rows={5} className="w-full border border-gray-300 rounded p-2"></textarea>
          </div>
          <button type="button" onClick={() => alert('UI only')} className="w-full bg-orange-500 hover:bg-orange-600 text-white font-bold py-3 px-6 rounded transition-colors">
            Submit Enquiry
          </button>
        </form>
      </div>
    </div>
  );
}
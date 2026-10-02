import os

base_dir = "/Users/samakshsingh/Documents/demo sports site"

def update_file(path, old, new):
    full = os.path.join(base_dir, path)
    with open(full, "r") as f:
        content = f.read()
    content = content.replace(old, new)
    with open(full, "w") as f:
        f.write(content)

# Fix Hero readability
page_path = "app/page.tsx"
with open(os.path.join(base_dir, page_path), "r") as f:
    page_content = f.read()

# Add a darker gradient and a text-shadow or box
old_hero = """
        <div className="absolute inset-0 bg-black/30 z-10" />
        
        <div className="relative z-20 text-center text-white px-4 flex flex-col items-center mt-12">
          <h1 className="text-4xl md:text-5xl font-serif font-bold mb-4 tracking-wide shadow-sm">{siteData.store.name}</h1>
          <p className="text-lg md:text-xl mb-10 font-light tracking-wider shadow-sm">{siteData.store.tagline}</p>
"""
new_hero = """
        <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/40 to-black/60 z-10" />
        
        <div className="relative z-20 text-center text-white px-8 py-10 flex flex-col items-center mt-12 bg-black/40 backdrop-blur-sm rounded-xl border border-white/10 max-w-2xl mx-auto shadow-2xl">
          <h1 className="text-4xl md:text-5xl font-serif font-bold mb-4 tracking-wide">{siteData.store.name}</h1>
          <p className="text-lg md:text-xl mb-10 font-light tracking-wider text-gray-200">{siteData.store.tagline}</p>
"""
if old_hero in page_content:
    update_file(page_path, old_hero, new_hero)


# Fix Next.js 15+ params promise issue in Products and Collections
def fix_params(path, param_name):
    full = os.path.join(base_dir, path)
    if not os.path.exists(full): return
    with open(full, "r") as f:
        content = f.read()
    
    # export default function ProductPage({ params }: { params: { slug: string } }) {
    #   const product = productsData.find(p => p.slug === params.slug);
    # =>
    # export default async function ProductPage({ params }: { params: Promise<{ slug: string }> }) {
    #   const { slug } = await params;
    
    import re
    
    # Change component signature to async and await params
    content = re.sub(
        r'export default function (\w+)\(\{ params \}: \{ params: \{ ([^:]+): string \} \}\) \{',
        r'export default async function \1({ params }: { params: Promise<{ \2: string }> }) {\n  const resolvedParams = await params;\n  const \2 = resolvedParams.\2;',
        content
    )
    
    # Replace params.slug with slug
    content = content.replace(f'params.{param_name}', param_name)
    
    with open(full, "w") as f:
        f.write(content)

fix_params("app/products/[slug]/page.tsx", "slug")
fix_params("app/collections/[category]/page.tsx", "category")

print("Fixed UI and params.")

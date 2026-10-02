# Patiala Sports House - Frontend

This is a modern, frontend-only e-commerce website for "Patiala Sports House". It is built with Next.js (App Router), TypeScript, and Tailwind CSS. The store has no backend or database; all data is managed via local JSON files.

## Setup Instructions

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Run the development server:**
   ```bash
   npm run dev
   ```
   Open [http://localhost:3000](http://localhost:3000) in your browser to see the result.

3. **Build for production:**
   ```bash
   npm run build
   ```

## Project Structure

- `app/`: Next.js App Router pages (Home, Collection, Product, Search, Static pages).
- `components/`: Reusable React components (Header, Footer, ProductCard, CartDrawer, etc.).
- `data/`: Local JSON data (`site.json`, `products.json`).
- `lib/`: Utility functions and context providers (CartContext).
- `public/images/`: Static assets and images.
- `types/`: TypeScript definitions.

## How to Edit Content

### 1. Store Details & Branding
Edit `data/site.json`. Here you can change:
- Store name, tagline, and short story
- Contact details (phone, email, address, hours)
- Announcement bar text
- Navigation categories and subcategories
- Brands list
- Testimonials
- Social media links (currently `#TODO`)
- **Note:** Changing the phone number here automatically updates the WhatsApp order links across the site.

### 2. Products
Edit `data/products.json`.
- Each product is an object containing `id`, `slug`, `name`, `price`, `description`, `category`, `imagePaths`, etc.
- To add a new product, copy an existing object and update the fields. Make sure the `slug` is unique.

### 3. Images and Media
- **Placeholders:** Currently, the site uses auto-generated placeholder images with solid colors.
- **Where to put real images:** Check `public/images/README.md` for a complete list of filenames.
- **Hero Video:** Replace `public/images/hero/hero-video-poster.webp` with a real poster image, and update the `<video>` tag in `app/page.tsx` to source your actual video file.

### 4. Code & Styling
- **Colors:** Defined in `app/globals.css` using Tailwind CSS v4 variables.
- **Components:** Modifying the Header, Footer, or Cart Drawer can be done inside the `components/` directory.

## What is Missing / Needs Replacement
- **Real Photos & Videos:** You must download real, un-watermarked Indian sports shop images from Unsplash/Pexels and replace the files in `public/images/`.
- **Social Links:** Update the Instagram and Facebook URLs in `site.json`.
- **WhatsApp Number:** Put your actual WhatsApp number in `site.json` `phone` field.
- **Real Reviews:** Replace the dummy testimonials in `site.json` with actual reviews from your customers.

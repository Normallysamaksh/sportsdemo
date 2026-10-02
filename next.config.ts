import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: "export",
  basePath: "/sportsdemo",
  images: {
    unoptimized: true,
  },
};

export default nextConfig;

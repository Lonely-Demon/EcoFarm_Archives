import type { Metadata, Viewport } from "next";
import "./globals.css";
import Nav from "@/components/Nav";
import ServiceWorker from "@/components/ServiceWorker";

export const metadata: Metadata = {
  title: {
    default: "EcoFarm — crop decision support for Namakkal",
    template: "%s · EcoFarm",
  },
  description:
    "Crop decision support for Namakkal blocks. Every result names its sources, shows what was excluded, and refuses to answer outside its tested scope.",
  applicationName: "EcoFarm",
  manifest: "/manifest.webmanifest",
  appleWebApp: {
    capable: true,
    statusBarStyle: "default",
    title: "EcoFarm",
  },
  icons: {
    icon: [
      { url: "/icons/favicon.svg", type: "image/svg+xml" },
      { url: "/icons/icon-192.png", sizes: "192x192", type: "image/png" },
    ],
    apple: [{ url: "/icons/icon-192.png", sizes: "192x192" }],
  },
  formatDetection: { telephone: false },
};

export const viewport: Viewport = {
  themeColor: "#4f7351",
  width: "device-width",
  initialScale: 1,
  maximumScale: 5,
  viewportFit: "cover",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <Nav />
        <main className="shell">{children}</main>
        <ServiceWorker />
      </body>
    </html>
  );
}

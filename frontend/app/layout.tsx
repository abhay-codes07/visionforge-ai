import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Visionary Agent Protocol",
  description: "Real-time Vision AI Agent platform",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

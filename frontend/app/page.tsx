import { FeaturedSection } from "@/components/home/featured";
import { HeroSection } from "@/components/home/hero";
import { Navbar } from "@/components/layout/navbar";

export default function HomePage() {
  return (
    <main className="min-h-screen bg-background text-foreground">
      <Navbar />
      <HeroSection />
      <FeaturedSection />
    </main>
  );
}

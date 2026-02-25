import { Brain, Lightning, VideoCamera } from "@phosphor-icons/react/dist/ssr";

import { Reveal } from "@/components/ui/reveal";
import { Section } from "@/components/ui/section";

const featuredItems = [
  {
    title: "Live Scene Intelligence",
    description: "Stream object detection and contextual scene summaries with sub-second visual reasoning.",
    icon: VideoCamera,
  },
  {
    title: "Agentic Automation",
    description: "Trigger workflows from natural-language vision insights across operations and support teams.",
    icon: Lightning,
  },
  {
    title: "Executive-Grade Control",
    description: "Unified oversight dashboards with transparent confidence signals and actionable recommendations.",
    icon: Brain,
  },
] as const;

export function FeaturedSection() {
  return (
    <Section id="features" className="pt-4">
      <Reveal className="mb-8">
        <p className="text-xs uppercase tracking-[0.32em] text-white/55">Featured</p>
        <h2 className="mt-3 text-3xl font-semibold tracking-tight sm:text-4xl">Built for Real-Time Vision Operations</h2>
      </Reveal>
      <div className="grid gap-5 md:grid-cols-3">
        {featuredItems.map((item, idx) => (
          <Reveal key={item.title} delay={idx * 0.08} className="glass-card rounded-2xl p-6">
            <item.icon size={24} className="mb-4 text-cyan-300" />
            <h3 className="text-lg font-semibold text-white/95">{item.title}</h3>
            <p className="mt-2 text-sm text-white/68">{item.description}</p>
          </Reveal>
        ))}
      </div>
    </Section>
  );
}

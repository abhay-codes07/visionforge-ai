import { ChartLineUp, Eye, GlobeHemisphereWest, ShieldCheck, Timer, WaveSine } from "@phosphor-icons/react/dist/ssr";

import { Reveal } from "@/components/ui/reveal";
import { Section } from "@/components/ui/section";

const features = [
  {
    title: "Multimodal Vision Ingestion",
    description: "Analyze still images, live webcam feeds, and recorded video through one unified interface.",
    icon: Eye,
  },
  {
    title: "Streaming Agent Responses",
    description: "Receive incremental, token-level vision insights as the model reasons in real-time.",
    icon: WaveSine,
  },
  {
    title: "Operational SLA Monitoring",
    description: "Track latency, throughput, and confidence metrics with real-time performance visibility.",
    icon: Timer,
  },
  {
    title: "Enterprise Security Ready",
    description: "Role-ready architecture with isolated service boundaries and future auth extensibility.",
    icon: ShieldCheck,
  },
  {
    title: "Global Edge Awareness",
    description: "Design supports distributed capture points for geographically distributed operations.",
    icon: GlobeHemisphereWest,
  },
  {
    title: "Decision Intelligence",
    description: "Convert visual observations into strategic recommendations and action triggers.",
    icon: ChartLineUp,
  },
] as const;

export function FeaturesGridSection() {
  return (
    <Section>
      <Reveal className="mb-8">
        <p className="text-xs uppercase tracking-[0.32em] text-white/55">Platform Features</p>
        <h2 className="mt-3 text-3xl font-semibold tracking-tight sm:text-4xl">Purpose-Built for Vision-First Teams</h2>
      </Reveal>

      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {features.map((feature, idx) => (
          <Reveal
            key={feature.title}
            delay={idx * 0.06}
            className="glass-card group rounded-2xl border border-white/10 p-6 transition hover:border-cyan-300/30"
          >
            <feature.icon size={22} className="text-cyan-300" />
            <h3 className="mt-4 text-lg font-semibold text-white/92">{feature.title}</h3>
            <p className="mt-2 text-sm leading-relaxed text-white/66">{feature.description}</p>
          </Reveal>
        ))}
      </div>
    </Section>
  );
}

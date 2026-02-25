import { Reveal } from "@/components/ui/reveal";
import { Section } from "@/components/ui/section";

const missionMetrics = [
  { label: "Mean Analysis Latency", value: "420ms" },
  { label: "Visual Event Coverage", value: "99.2%" },
  { label: "Team Response Time Gain", value: "3.4x" },
] as const;

export function MissionSection() {
  return (
    <Section>
      <Reveal className="glass-card rounded-3xl overflow-hidden p-8 sm:p-12">
        <p className="text-xs uppercase tracking-[0.32em] text-white/55">Mission</p>
        <h2 className="mt-3 max-w-3xl text-3xl font-semibold tracking-tight sm:text-4xl">
          Bring executive-grade visual intelligence to every frontline decision.
        </h2>
        <p className="mt-4 max-w-3xl text-sm leading-relaxed text-white/68 sm:text-base">
          Visionary Agent Protocol was built to close the gap between raw camera data and decisive action. We are
          engineering a real-time AI control layer where every visual signal becomes immediate, auditable, and useful.
        </p>

        <div className="mt-8 grid gap-4 sm:grid-cols-3">
          {missionMetrics.map((metric, idx) => (
            <Reveal
              key={metric.label}
              delay={0.05 * idx}
              className="rounded-2xl border border-white/12 bg-white/[0.03] p-5"
            >
              <p className="text-xs uppercase tracking-[0.2em] text-white/50">{metric.label}</p>
              <p className="mt-3 text-2xl font-semibold text-cyan-200">{metric.value}</p>
            </Reveal>
          ))}
        </div>
      </Reveal>
    </Section>
  );
}

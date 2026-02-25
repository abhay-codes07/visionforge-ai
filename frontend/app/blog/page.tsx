import { ClockCountdown, Sparkle } from "@phosphor-icons/react/dist/ssr";

import { PageShell } from "@/components/layout/page-shell";
import { Reveal } from "@/components/ui/reveal";
import { Section } from "@/components/ui/section";

const articles = [
  {
    title: "Designing Real-Time Vision Agent Loops for Operations Teams",
    date: "February 25, 2026",
    readTime: "6 min read",
    content:
      "Production vision systems fail when teams treat inference as a batch process. Real-time loops require streaming context, confidence-aware UX, and deterministic action routing. Visionary Agent Protocol was designed to keep operators in control while AI handles perception at machine speed.",
  },
  {
    title: "Why Glassmorphic Interface Patterns Improve AI Trust",
    date: "February 20, 2026",
    readTime: "4 min read",
    content:
      "High-stakes AI interfaces need visual hierarchy that emphasizes signal over noise. Our design language uses layered glass surfaces, restrained motion, and low-opacity secondary text so users can scan decisions quickly without cognitive overload.",
  },
  {
    title: "WebSockets vs Polling for Live Vision Intelligence",
    date: "February 14, 2026",
    readTime: "5 min read",
    content:
      "Polling creates blind spots and latency spikes when visual context changes rapidly. Streaming over WebSockets enables token-level updates, near-instant anomaly alerts, and tighter operator feedback loops. For vision-first workflows, push beats pull.",
  },
  {
    title: "From Prototype to Platform: Hardening Multimodal AI Systems",
    date: "February 9, 2026",
    readTime: "7 min read",
    content:
      "Moving beyond demo quality means investing in modular service boundaries, environment-driven config, and observability from day one. The winning pattern is simple: isolate model integrations, keep contracts explicit, and design UI states for partial failure.",
  },
] as const;

export default function BlogPage() {
  return (
    <PageShell
      title="Blog"
      subtitle="Insights on building production-grade vision systems, premium AI interfaces, and real-time agent architectures."
    >
      <Section className="pt-2">
        <div className="grid gap-5">
          {articles.map((article, idx) => (
            <Reveal key={article.title} delay={idx * 0.06} className="glass-card rounded-2xl p-6 sm:p-7">
              <div className="mb-4 flex flex-wrap items-center gap-3 text-xs text-white/56">
                <span className="inline-flex items-center gap-1.5 rounded-full border border-white/12 bg-white/[0.03] px-3 py-1">
                  <ClockCountdown size={12} />
                  {article.readTime}
                </span>
                <span>{article.date}</span>
              </div>
              <h2 className="text-2xl font-semibold tracking-tight text-white/94">{article.title}</h2>
              <p className="mt-3 text-sm leading-relaxed text-white/70">{article.content}</p>
              <button
                type="button"
                className="mt-5 inline-flex items-center gap-2 rounded-lg border border-white/20 px-3.5 py-2 text-xs font-medium text-white/85 transition hover:border-cyan-300/45 hover:text-white"
              >
                Read full article <Sparkle size={12} />
              </button>
            </Reveal>
          ))}
        </div>
      </Section>
    </PageShell>
  );
}

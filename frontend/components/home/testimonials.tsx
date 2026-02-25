"use client";

import { CaretLeft, CaretRight, Quotes } from "@phosphor-icons/react";
import { AnimatePresence, motion } from "framer-motion";
import { useMemo, useState } from "react";

import { Section } from "@/components/ui/section";

const testimonials = [
  {
    quote:
      "Visionary Agent Protocol reduced manual visual QA by 67% in our first week. The live reasoning stream is genuinely production-ready.",
    author: "Elena Torres",
    role: "VP Product, Helios Freight",
  },
  {
    quote:
      "Our operations team finally has one pane of glass for camera feeds, anomaly alerts, and AI-suggested actions. The speed is exceptional.",
    author: "Marcus Lee",
    role: "Head of Ops, Northline Robotics",
  },
  {
    quote:
      "It feels like a premium mission-control product, not a prototype. We were shipping new workflows on day one.",
    author: "Priya Narang",
    role: "Founder, Atlas Vision Systems",
  },
] as const;

export function TestimonialsSection() {
  const [index, setIndex] = useState(0);
  const total = testimonials.length;
  const active = useMemo(() => testimonials[index], [index]);

  const next = () => setIndex((prev) => (prev + 1) % total);
  const prev = () => setIndex((prev) => (prev - 1 + total) % total);

  return (
    <Section>
      <div className="glass-card rounded-3xl p-6 sm:p-10">
        <div className="mb-8 flex items-center justify-between">
          <div>
            <p className="text-xs uppercase tracking-[0.35em] text-white/55">Testimonials</p>
            <h2 className="mt-3 text-3xl font-semibold tracking-tight sm:text-4xl">Trusted by Fast-Moving Teams</h2>
          </div>
          <div className="hidden gap-2 sm:flex">
            <button
              type="button"
              onClick={prev}
              className="inline-flex h-10 w-10 items-center justify-center rounded-xl border border-white/20 text-white/80 transition hover:border-white/35 hover:text-white"
              aria-label="Previous testimonial"
            >
              <CaretLeft size={16} />
            </button>
            <button
              type="button"
              onClick={next}
              className="inline-flex h-10 w-10 items-center justify-center rounded-xl border border-white/20 text-white/80 transition hover:border-white/35 hover:text-white"
              aria-label="Next testimonial"
            >
              <CaretRight size={16} />
            </button>
          </div>
        </div>

        <AnimatePresence mode="wait">
          <motion.article
            key={active.author}
            initial={{ opacity: 0, y: 12 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -12 }}
            transition={{ duration: 0.35, ease: "easeOut" }}
            className="rounded-2xl border border-white/10 bg-white/[0.02] p-6"
          >
            <Quotes size={26} className="mb-4 text-cyan-300" weight="fill" />
            <p className="text-lg leading-relaxed text-white/88">{active.quote}</p>
            <p className="mt-6 text-sm font-semibold text-white/90">{active.author}</p>
            <p className="mt-1 text-sm text-white/60">{active.role}</p>
          </motion.article>
        </AnimatePresence>

        <div className="mt-6 flex items-center justify-center gap-2">
          {testimonials.map((item, dotIndex) => (
            <button
              key={item.author}
              type="button"
              onClick={() => setIndex(dotIndex)}
              className={`h-2.5 rounded-full transition ${
                dotIndex === index ? "w-8 bg-cyan-300" : "w-2.5 bg-white/30 hover:bg-white/50"
              }`}
              aria-label={`Go to testimonial ${dotIndex + 1}`}
            />
          ))}
        </div>
      </div>
    </Section>
  );
}

<h1 align="center">Vivens B</h1>

<p align="center">
  Software engineer working across full-stack TypeScript and embedded systems.<br/>
  Kigali, Rwanda.
</p>

<p align="center">
  <a href="https://vivens.pro">vivens.pro</a>
</p>

---

### What I build

**Product engineering.** React Native and Expo apps, Next.js App Router and Nuxt 3 on the web, Postgres behind Drizzle or Supabase. Auth, payments, multi-tenant data models, the parts that have to keep working.

**Embedded and telematics.** ESP32 and Arduino firmware, GSM and GPRS modules (A9G, A7670, SIM7600), GPS tracking and RFID. Vehicle tracking is where the two halves meet: firmware that holds a session on a flaky network, and an app that makes the data useful.

**Applied AI.** LLM features in production apps using the Vercel AI SDK, retrieval, and tracing with Langfuse.

---

### Open source

I answer technical questions upstream, and I reproduce things before posting rather than reasoning from memory. Recent work:

- **[tailwindcss#20443](https://github.com/tailwindlabs/tailwindcss/discussions/20443)**<br/>
  bisected a CSS nesting regression across five releases and pinned it to v4.3.3, where `&__element` began compiling to an invalid selector that later tooling silently drops.
- **[supabase#49709](https://github.com/supabase/supabase/discussions/49709)**<br/>
  reproduced a row-level security `42501` across seven policy configurations on PostgreSQL 16, and showed that whether the error names a policy tells you which half of the policy set failed.
- **[better-auth#11026](https://github.com/better-auth/better-auth/discussions/11026)**<br/>
  demonstrated that `SET search_path` on a shared connection pool leaks across tenants, and verified the alternative keeps tenants isolated on a single reused connection.
- **[trpc#7528](https://github.com/trpc/trpc/discussions/7528)**<br/>
  traced which branches of a duplicated test helper were genuinely uncovered, then wrote the patch that closes the gap without widening the package's public API.
- **[pnpm#14282](https://github.com/pnpm/pnpm/discussions/14282)**<br/>
  established which `bin` entry `pnpm create` resolves, with the negative case that proves the name match is required. *Accepted answer.*

---

### Stack

<p>
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=white" />
  <img src="https://img.shields.io/badge/React_Native-61DAFB?style=flat&logo=react&logoColor=black" />
  <img src="https://img.shields.io/badge/Expo-000020?style=flat&logo=expo&logoColor=white" />
  <img src="https://img.shields.io/badge/Next.js-000000?style=flat&logo=next.js&logoColor=white" />
  <img src="https://img.shields.io/badge/Nuxt-00DC82?style=flat&logo=nuxt.js&logoColor=white" />
  <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat&logo=tailwind-css&logoColor=white" />
</p>
<p>
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Supabase-3FCF8E?style=flat&logo=supabase&logoColor=white" />
  <img src="https://img.shields.io/badge/Drizzle-C5F74F?style=flat&logo=drizzle&logoColor=black" />
  <img src="https://img.shields.io/badge/NestJS-E0234E?style=flat&logo=nestjs&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white" />
</p>
<p>
  <img src="https://img.shields.io/badge/ESP32-E7352C?style=flat&logo=espressif&logoColor=white" />
  <img src="https://img.shields.io/badge/Arduino-00979D?style=flat&logo=arduino&logoColor=white" />
  <img src="https://img.shields.io/badge/C++-00599C?style=flat&logo=cplusplus&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" />
</p>

---

<p align="center">
  <a href="https://vivens.pro">vivens.pro</a> ·
  <a href="mailto:vivens.byiringiro77@gmail.com">email</a>
</p>

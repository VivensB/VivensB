<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/banner-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/banner-light.svg">
  <img alt="Vivens B, full-stack TypeScript and embedded telematics, Kigali Rwanda" src="./assets/banner-dark.svg" width="100%">
</picture>

<br/>

I build and ship software products for the Rwandan market, mostly multi-tenant SaaS,
and I work at both ends of the stack: the firmware that reports a vehicle's position
over a patchy GSM network, and the interface someone uses to act on it.

<br/>

## What I ship

<table>
<tr><td width="50%" valign="top">

### 🎓 School management
**SchoolHub** · **ZiSchool**

Multi-tenant MIS for primary and secondary schools. Enrolment, transcripts,
reporting. Fastify and Prisma on Postgres, Vue 3 and Next.js clients,
per-tenant data isolation.

</td><td width="50%" valign="top">

### 🛰 Vehicle telematics
**Moto-Track**

Tracking for Rwanda's moto economy, end to end. GSM firmware, ingest server,
ERP, admin console, and an Expo app with MapLibre. Nx monorepo.

</td></tr>
<tr><td width="50%" valign="top">

### 🚨 Roadside assistance
**Roadside Assistant**

Dispatch platform. Fastify with WebSockets for live driver position,
React Native app for responders, Next.js console for operators.

</td><td width="50%" valign="top">

### 💼 Business & training
**Boostly** · **SmartLinkRwanda**

SME tooling and an IT training and certification platform.
Next.js, Drizzle, Supabase.

</td></tr>
</table>

<br/>

## Stack

**Web**
<br/>
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" />
<img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white" />
<img src="https://img.shields.io/badge/Nuxt-00DC82?style=flat-square&logo=nuxtdotjs&logoColor=white" />
<img src="https://img.shields.io/badge/Vue_3-4FC08D?style=flat-square&logo=vuedotjs&logoColor=white" />
<img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black" />
<img src="https://img.shields.io/badge/TanStack_Query-FF4154?style=flat-square&logo=reactquery&logoColor=white" />
<img src="https://img.shields.io/badge/Tailwind-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white" />

**Mobile**
<br/>
<img src="https://img.shields.io/badge/Expo-000020?style=flat-square&logo=expo&logoColor=white" />
<img src="https://img.shields.io/badge/React_Native-61DAFB?style=flat-square&logo=react&logoColor=black" />
<img src="https://img.shields.io/badge/MapLibre-295DAA?style=flat-square&logo=maplibre&logoColor=white" />
<img src="https://img.shields.io/badge/Reanimated-001A72?style=flat-square&logo=react&logoColor=white" />

**Backend & data**
<br/>
<img src="https://img.shields.io/badge/Fastify-000000?style=flat-square&logo=fastify&logoColor=white" />
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" />
<img src="https://img.shields.io/badge/Prisma-2D3748?style=flat-square&logo=prisma&logoColor=white" />
<img src="https://img.shields.io/badge/Drizzle-C5F74F?style=flat-square&logo=drizzle&logoColor=black" />
<img src="https://img.shields.io/badge/Supabase-3FCF8E?style=flat-square&logo=supabase&logoColor=white" />
<img src="https://img.shields.io/badge/Neon-00E599?style=flat-square&logo=neon&logoColor=black" />
<img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white" />

**Embedded**
<br/>
<img src="https://img.shields.io/badge/ESP32-E7352C?style=flat-square&logo=espressif&logoColor=white" />
<img src="https://img.shields.io/badge/Arduino-00979D?style=flat-square&logo=arduino&logoColor=white" />
<img src="https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white" />
<img src="https://img.shields.io/badge/GSM_%2F_GPRS-5A5A5A?style=flat-square&logoColor=white" />

**Tooling**
<br/>
<img src="https://img.shields.io/badge/Nx-143055?style=flat-square&logo=nx&logoColor=white" />
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" />
<img src="https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white" />
<img src="https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white" />

<br/>

## Open source

I answer upstream, and I reproduce before I post rather than reasoning from memory.

<table>
<tr><td><a href="https://github.com/tailwindlabs/tailwindcss/discussions/20443"><b>tailwindcss #20443</b></a></td>
<td>Bisected a CSS nesting regression across five releases to v4.3.3, where <code>&amp;__element</code> starts compiling to an invalid selector that later tooling silently drops.</td></tr>

<tr><td><a href="https://github.com/supabase/supabase/discussions/49709"><b>supabase #49709</b></a></td>
<td>Reproduced an RLS <code>42501</code> across seven policy configurations on PostgreSQL 16, and showed that whether the error names a policy tells you which half of the policy set failed.</td></tr>

<tr><td><a href="https://github.com/better-auth/better-auth/discussions/11026"><b>better-auth #11026</b></a></td>
<td>Demonstrated that <code>SET search_path</code> on a shared pool leaks across tenants, and verified the alternative keeps them isolated on one reused connection.</td></tr>

<tr><td><a href="https://github.com/trpc/trpc/discussions/7528"><b>trpc #7528</b></a></td>
<td>Traced which branches of a duplicated test helper were genuinely uncovered, then wrote the patch that closes the gap without widening the package's public API.</td></tr>

<tr><td><a href="https://github.com/pnpm/pnpm/discussions/14282"><b>pnpm #14282</b></a></td>
<td>Established which <code>bin</code> entry <code>pnpm create</code> resolves, with the negative case proving the name match is required. <b>Accepted answer.</b></td></tr>
</table>

<br/>

<p align="center">
  <a href="https://vivens.pro"><b>vivens.pro</b></a>
  &nbsp;·&nbsp;
  <a href="mailto:vivens.byiringiro77@gmail.com">vivens.byiringiro77@gmail.com</a>
</p>

"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const LINKS = [
  { href: "/", label: "Home", icon: "⌂" },
  { href: "/decide", label: "Decide", icon: "❋" },
  { href: "/sources", label: "Sources", icon: "◎" },
  { href: "/method", label: "Method", icon: "≡" },
];

function isActive(pathname: string, href: string) {
  if (href === "/") return pathname === "/";
  return pathname.startsWith(href);
}

export default function Nav() {
  const pathname = usePathname() || "/";

  return (
    <>
      <header className="topbar">
        <div className="topbar-inner">
          <Link href="/" className="brand">
            <span className="brand-mark" aria-hidden>
              ❋
            </span>
            EcoFarm
          </Link>
          <nav className="tabs" aria-label="Main">
            {LINKS.map((link) => (
              <Link key={link.href} href={link.href} data-active={isActive(pathname, link.href)}>
                {link.label}
              </Link>
            ))}
          </nav>
        </div>
      </header>

      <nav className="bottom-nav" aria-label="Main">
        <div className="bottom-nav-inner">
          {LINKS.map((link) => (
            <Link key={link.href} href={link.href} data-active={isActive(pathname, link.href)}>
              <span className="icon" aria-hidden>
                {link.icon}
              </span>
              {link.label}
            </Link>
          ))}
        </div>
      </nav>
    </>
  );
}

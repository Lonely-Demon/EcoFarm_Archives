import Link from "next/link";

export const metadata = { title: "Offline" };

export default function Offline() {
  return (
    <>
      <p className="eyebrow">No connection</p>
      <h1>EcoFarm needs a connection to compare crops.</h1>
      <p className="lede">
        A recommendation is never shown from an offline copy, because a stored comparison
        could be out of date and would look current. The app is still installed on your
        device — reopen it when you have a signal.
      </p>
      <div className="notice warn" style={{ marginTop: 18 }}>
        <span className="notice-icon" aria-hidden>
          ⚠
        </span>
        <div>
          <strong>Nothing current is being shown</strong>
          No older comparison, weather figure or price is being substituted for live data.
        </div>
      </div>
      <div style={{ marginTop: 18 }}>
        <Link href="/" className="btn secondary">
          Try again
        </Link>
      </div>
    </>
  );
}

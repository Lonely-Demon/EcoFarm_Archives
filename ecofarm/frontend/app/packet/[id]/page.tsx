import Link from "next/link";
import type { Metadata } from "next";
import PacketView from "@/components/PacketView";
import { fetchPacketServer, type DecisionPacket } from "@/lib/server-api";

export const dynamic = "force-dynamic";

export const metadata: Metadata = { title: "Decision packet" };

export default async function PacketPage({
  params,
  searchParams,
}: {
  params: Promise<{ id: string }>;
  searchParams: Promise<{ fresh?: string }>;
}) {
  const { id } = await params;
  const { fresh } = await searchParams;

  let packet: DecisionPacket | null = null;
  let failure: { state: string; message: string } | null = null;

  try {
    packet = await fetchPacketServer(id);
  } catch (error) {
    const err = error as { state?: string; message?: string };
    failure = {
      state: err.state ?? "unavailable",
      message:
        err.message ??
        "The decision service could not be reached, so no comparison is being shown.",
    };
  }

  if (!packet) {
    const expired = failure?.state === "not_found_or_expired";
    return (
      <>
        <p className="eyebrow" style={{ marginTop: 24 }}>
          Decision packet
        </p>
        <h1>{expired ? "This decision record is not available." : "Cannot show this comparison."}</h1>
        <div className="notice stop" style={{ marginTop: 14 }}>
          <span className="notice-icon" aria-hidden>
            ⚠
          </span>
          <div>
            <strong>
              {expired
                ? "It may have passed its 90-day retention period, or been deleted."
                : "Nothing current could be loaded"}
            </strong>
            {failure?.message}
            <p className="small" style={{ margin: "8px 0 0" }}>
              EcoFarm deliberately does not render an older or cached comparison in place of
              the missing one, because a stored result would look current when it is not.
            </p>
          </div>
        </div>
        <div className="btn-row" style={{ marginTop: 18 }}>
          <Link href="/decide" className="btn">
            Start a new decision
          </Link>
          <Link href="/sources" className="btn secondary">
            Check source status
          </Link>
        </div>
      </>
    );
  }

  return <PacketView packet={packet} fresh={fresh === "1"} />;
}

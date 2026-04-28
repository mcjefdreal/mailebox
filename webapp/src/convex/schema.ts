import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  mailboxes: defineTable({
    locker_number: v.float64(),
    recipient_uid: v.string(),
    recipient_name: v.string(),
    delivered_by: v.string(),
    claim_by: v.string(),
    status: v.string(),
  }),
});
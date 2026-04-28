import { query } from "./_generated/server.js";
// import { v } from "convex/values";

export const getMailboxes = query({
    args: {},
    handler: async (ctx) => {
        // Get most recent messages first
        const mailboxes = await ctx.db.query("mailboxes").collect();
        // Reverse the list so that it's in a chronological order.
        console.log(mailboxes)
        return mailboxes;
    },
});
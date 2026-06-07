import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

/**
 * Publications collection.
 * Each work is one Markdown file in src/content/publications/.
 * To add a new publication, copy any file there and edit the frontmatter.
 */
const publications = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/publications" }),
  schema: z.object({
    title: z.string(),
    year: z.number(),
    venue: z.string(),
    type: z.enum(["book", "chapter", "article", "review"]),
    coauthors: z.array(z.string()).optional(),
    url: z.string().url().optional(),
    /** higher = listed first within the same year */
    order: z.number().default(0),
    /** show as "Forthcoming" and sort to the very top */
    forthcoming: z.boolean().default(false),
    summary: z.string(),
  }),
});

export const collections = { publications };

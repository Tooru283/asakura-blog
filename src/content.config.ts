import { defineCollection, z } from 'astro:content'
import { glob } from "astro/loaders";

const blogCollection = defineCollection({
    loader: glob({ pattern: '**/[^_]*.md', base: "./src/content/blog" }),
    schema: z.object({
        title: z.string(),
        pubDate: z.date(),
        draft: z.boolean().optional().default(false),
        description: z.string().optional().default(''),
        image: z.string().optional().default(''),
        slugId: z.string(),
        category: z.string().optional(),
    }),
})

const specCollection = defineCollection({
    loader: glob({ pattern: '**/[^_]*.md', base: "./src/content/spec" }),
})

const fragmentsCollection = defineCollection({
    loader: glob({ pattern: '**/[^_]*.md', base: "./src/content/fragments" }),
    schema: z.object({
        date: z.date(),
        image: z.string().optional(),
    }),
})

export const collections = {
    blog: blogCollection,
    spec: specCollection,
    fragments: fragmentsCollection,
}
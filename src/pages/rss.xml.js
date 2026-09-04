import { getCollection } from 'astro:content';

export async function GET() {
  const posts = await getCollection('blog');
  const sortedPosts = posts.sort((a, b) => new Date(b.data.pubDate).getTime() - new Date(a.data.pubDate).getTime());

  const rssItems = sortedPosts.map((post) => `
    <item>
      <title><![CDATA[${post.data.title}]]></title>
      <description><![CDATA[${post.data.description}]]></description>
      <link>https://brasizechecker.com/blog/${post.id}</link>
      <guid isPermaLink="true">https://brasizechecker.com/blog/${post.id}</guid>
      <pubDate>${new Date(post.data.pubDate).toUTCString()}</pubDate>
    </item>
  `).join('');

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>BraSizeChecker Blog & Fit Guides</title>
    <description>Expert guides, bra size calculators, and international sizing conversions.</description>
    <link>https://brasizechecker.com/blog</link>
    <atom:link href="https://brasizechecker.com/rss.xml" rel="self" type="application/rss+xml" />
    <language>en-us</language>
    <lastBuildDate>${new Date().toUTCString()}</lastBuildDate>
    ${rssItems}
  </channel>
</rss>`;

  return new Response(xml, {
    headers: {
      'Content-Type': 'application/xml; charset=utf-8',
    },
  });
}

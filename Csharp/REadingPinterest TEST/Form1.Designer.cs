
using Microsoft.Web.WebView2.WinForms;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;
namespace REadingPinterest_TEST
{

    public partial class Form1 : Form
    {
        private WebView2 webView;
        private TextBox textBox;

        private Dictionary<string, int> wordCounts = new Dictionary<string, int>();
        private Dictionary<string, int> phraseCounts = new Dictionary<string, int>();
        private System.Windows.Forms.Timer scrapeTimer;
        public Form1()
        {
            InitializeComponent();

            webView = new WebView2()
            {
                Dock = DockStyle.Fill,
            };

            Controls.Add(webView);
            textBox = new TextBox
            {
                Multiline = true,
                ReadOnly = true,
                Dock = DockStyle.Bottom,
                Height = 200,
                ScrollBars = ScrollBars.Vertical
            };

            Controls.Add(textBox);
            Load += async (s, e) =>
            {
                await webView.EnsureCoreWebView2Async();
                webView.Source = new Uri("https://cz.pinterest.com/pin/789959590927772293/");

                webView.NavigationCompleted += (_, _) =>
                {
                    StartScraping();
                };
            };
        }

        private void StartScraping()
        {
            scrapeTimer = new System.Windows.Forms.Timer();
            scrapeTimer.Interval = 2000;
            scrapeTimer.Tick += async (s, e) =>
            {
                string jsCode = @"
(() => {
  // Initialize a set to track processed texts
  if (!window._processedTexts) {
    window._processedTexts = new Set();
  }

  // Define stop words to exclude common irrelevant terms
  const stopWords = new Set([
    'the', 'a', 'an', 'in', 'on', 'and', 'of', 'to', 'with', 'for',
    'is', 'by', 'pin', 'post', 'pinterest', 'image', 'photo', 'story',
    'avatar', 'link', 'this', 'that', 'these', 'those', 'it', 'its',
    'follow', 'save', 'board', 'collection', 'profile', 'share', 'comment',
    'like', 'try', 'more', 'ideas', 'following', 'followers', 'created',
    'saved', 'view', 'all', 'posts', 'likes', 'comments', 'views',
    'shares', 'trending', 'popular', 'new', 'related', 'suggested',
    'menu', 'search', 'home', 'explore', 'messages', 'notifications',
    'settings', 'help', 'about', 'terms', 'privacy', 'copyright',
    'cookies', 'www', 'http', 'https', 'com', 'net', 'org'
  ]);

  // Function to determine if text is relevant
  function isWorthyText(text) {
    if (window._processedTexts.has(text)) return false;
    if (text.length < 3) return false;
    if (text.startsWith('/')) return false;

    const words = text.split(/\s+/);
    if (words.length === 1) {
      return !stopWords.has(text.toLowerCase());
    }

    const fashionTerms = ['shoe', 'outfit', 'style', 'fashion', 'wear', 'clothes',
                          'trend', 'design', 'jacket', 'pants', 'jeans', 'dress'];

    return fashionTerms.some(term => text.toLowerCase().includes(term));
  }

  // Function to check if an element is within a comment section
  function isInCommentSection(element) {
    return element.closest('.comment') || element.closest('.comments') ||
           element.closest('.comment-section') || element.closest('[data-test-id=""comments""]');
  }

  const newUniquePhrases = new Set();

  // Selectors for content to extract
  const contentSelectors = [
    'h1',
    '[data-test-id=""pin-title""]',
    '[data-test-id=""pinTitle""]',
    '[data-test-id=""pin-description""]',
    '[data-test-id=""pinDescription""]',
    '.tBJ.dyH.iFc.SMy.yTZ.pBj.DrD.IZT.swG',
    '.lH1.dyH.iFc.SMy.yTZ.pBj.DrD.IZT',
    '.tBJ.dyH.iFc.SMy.yTZ.pBj.DrD.mWe',
    '.lH1.dyH.iFc.SMy.yTZ.pBj.DrD.mWe'
  ];

  // Extract text from main content elements
  contentSelectors.forEach(selector => {
    document.querySelectorAll(selector).forEach(element => {
      if (isInCommentSection(element)) return;
      const text = element.textContent.trim();
      if (text && isWorthyText(text)) {
        newUniquePhrases.add(text);
        window._processedTexts.add(text);
      }
    });
  });

  // Extract alt text from images, excluding those in comment sections
  document.querySelectorAll('img[alt]:not([alt=""""])').forEach(img => {
    if (isInCommentSection(img)) return;
    const altText = img.alt.trim();
    if (altText && altText !== ""image"" && isWorthyText(altText)) {
      newUniquePhrases.add(altText);
      window._processedTexts.add(altText);

      const altWords = altText.split(/\s+/);
      altWords.forEach(word => {
        const cleanWord = word.replace(/[^\w\s'-]/g, '').trim();
        if (cleanWord.length > 3 && !stopWords.has(cleanWord.toLowerCase()) && isWorthyText(cleanWord)) {
          newUniquePhrases.add(cleanWord);
          window._processedTexts.add(cleanWord);
        }
      });
    }
  });

  // Extract text from other relevant elements, excluding those in comment sections
  const textElements = document.querySelectorAll('p, h2, h3, h4, span.pBj');
  textElements.forEach(el => {
    if (isInCommentSection(el)) return;
    const text = el.textContent.trim();
    if (text.length > 15 && isWorthyText(text)) {
      newUniquePhrases.add(text);
      window._processedTexts.add(text);

      const phrases = text.split(/[,.;:!?]/);
      phrases.forEach(phrase => {
        const trimmedPhrase = phrase.trim();
        if (trimmedPhrase.length > 5 && isWorthyText(trimmedPhrase)) {
          newUniquePhrases.add(trimmedPhrase);
          window._processedTexts.add(trimmedPhrase);
        }
      });
    }
  });

  if (newUniquePhrases.size === 0) {
    return JSON.stringify([""--COMPLETE--""]);
  }

   const wordSet = new Set();
newUniquePhrases.forEach(phrase => {
  phrase.split(/\s+/).forEach(word => {
    const clean = word.toLowerCase().replace(/[^\w'-]/g, '');
    if (clean.length > 2 && !stopWords.has(clean)) {
      wordSet.add(clean);
    }
  });
});


 return JSON.stringify({
    phrases: Array.from(newUniquePhrases),  // phrases
    words: Array.from(wordSet)              // single words extracted from phrases
});
    })();


                ";

                string result = await webView.ExecuteScriptAsync(jsCode);



                var parsed = System.Text.Json.JsonDocument.Parse(result);
                System.Diagnostics.Debug.WriteLine("Raw result: " + result);
                var root = parsed.RootElement;
                bool updated = false;
                if (root.TryGetProperty("phrases", out var phrasesJson))
                {
                    updated = true;
                    foreach (var phrase in phrasesJson.EnumerateArray())
                    {
                        string phraseStr = phrase.GetString().ToLowerInvariant();
                        if (phraseCounts.ContainsKey(phraseStr))
                            phraseCounts[phraseStr]++;
                        else
                            phraseCounts[phraseStr] = 1;
                    }
                }

                // Words
                if (root.TryGetProperty("words", out var wordsJson))
                {
                    updated = true;
                    foreach (var word in wordsJson.EnumerateArray())
                    {
                        string wordStr = word.GetString().ToLowerInvariant();
                        if (wordCounts.ContainsKey(wordStr))
                            wordCounts[wordStr]++;
                        else
                            wordCounts[wordStr] = 1;
                    }
                }


                // Check if scraping is complete
                if (result.Contains("--COMPLETE--"))
                {


                    textBox.Text += Environment.NewLine + "--- Scraping Complete ---";

                }

                var newWords = result
                    .Split(new[] { "\",\"", "\",", ",\"" }, StringSplitOptions.RemoveEmptyEntries)
                    .Select(w => w.Trim().ToLower())
                    .Where(w => !string.IsNullOrWhiteSpace(w));




                if (updated)
                {
                    textBox.Text = string.Join(Environment.NewLine,
                        wordCounts.OrderByDescending(key => key.Value)
                        .Select(kv => $"{kv.Key}: {kv.Value}"));
                }
            };
            scrapeTimer.Start();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}

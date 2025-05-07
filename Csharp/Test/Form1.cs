using Microsoft.Web.WebView2.WinForms;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;
using System.Text.Json;
using System.Text.Json.Nodes;
namespace Test
{

    public partial class Form1 : Form
    {
        private WebView2 webView;
        private TextBox wordsTextBox;
        private TextBox phrasesTextBox;

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
            wordsTextBox = new TextBox
            {
                Multiline = true,
                ReadOnly = true,
                Dock = DockStyle.Left,
                Width = this.ClientSize.Width / 2,
                ScrollBars = ScrollBars.Vertical
            };
            phrasesTextBox = new TextBox
            {
                Multiline = true,
                ReadOnly = true,
                Dock = DockStyle.Right,
                Width = this.ClientSize.Width / 2,
                ScrollBars = ScrollBars.Vertical
            };


            Controls.Add(wordsTextBox);
            Controls.Add(phrasesTextBox);
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
            scrapeTimer.Interval = 250;
            scrapeTimer.Tick += async (s, e) =>
            {
                string jsCode = @"
(() => {
  if (!window._processedTexts) {
    window._processedTexts = new Set();
  }

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
    'cookies', 'www', 'http', 'https', 'com', 'net', 'org',

    // custom blocked words (non-helpful terms)
    'outfit', 'outfits', 'inspo', 'inspiration', 'aesthetic', 'style', 'styles',
    'content', 'creator', 'photos', 'closet', 'mode', 'moodboard', 'dream', 'fashion'
  ]);

  function isWorthyText(text) {
    if (window._processedTexts.has(text)) return false;
    if (text.length < 3) return false;
    if (text.startsWith('/')) return false;

    const words = text.split(/\s+/);
    if (words.length === 1) {
      return !stopWords.has(text.toLowerCase());
    }

    const pluralFashionTerms = ['shoes', 'sneakers', 'jackets', 'jeans', 'slides', 'trainers', 'clothes', 'clogs', 'sandals'];
    return pluralFashionTerms.some(term => text.toLowerCase().includes(term));
  }

  function isInCommentSection(element) {
    return element.closest('.comment') || element.closest('.comments') ||
           element.closest('.comment-section') || element.closest('[data-test-id=""comments""]');
  }

  const newUniquePhrases = new Set();

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

  document.querySelectorAll('img[alt]:not([alt=""""])').forEach(img => {
    if (isInCommentSection(img)) return;
    const altText = img.alt.trim();
    if (altText && isWorthyText(altText)) {
      newUniquePhrases.add(altText);
      window._processedTexts.add(altText);

      const altWords = altText.split(/\s+/);
      altWords.forEach(word => {
        const clean = word.toLowerCase().replace(/[^\w'-]/g, '');
        if (clean.length > 3 && !stopWords.has(clean)) {
          newUniquePhrases.add(clean);
          window._processedTexts.add(clean);
        }
      });
    }
  });

  const textElements = document.querySelectorAll('p, h2, h3, h4, span.pBj');
  textElements.forEach(el => {
    if (isInCommentSection(el)) return;
    const text = el.textContent.trim();
    if (text.length > 15 && isWorthyText(text)) {
      const parts = text.split(/[,.;:!?]/);
      parts.forEach(part => {
        const words = part.trim().split(/\s+/).filter(w => w.length > 2);
        for (let i = 0; i < words.length; i++) {
          for (let len = 2; len <= 4; len++) {
            if (i + len <= words.length) {
              const phraseWords = words.slice(i, i + len);
              const cleanPhrase = phraseWords
                .map(w => w.toLowerCase().replace(/[^\w'-]/g, ''))
                .filter(w => w && !stopWords.has(w))
                .join(' ');
              if (cleanPhrase.split(' ').length >= 2 && isWorthyText(cleanPhrase)) {
                newUniquePhrases.add(cleanPhrase);
                window._processedTexts.add(cleanPhrase);
              }
            }
          }
        }
      });
    }
  });

  // Extract final unique words (plural normalized)
  const wordSet = new Set();
  newUniquePhrases.forEach(phrase => {
    phrase.split(/\s+/).forEach(word => {
      const clean = word.toLowerCase().replace(/[^\w'-]/g, '');
      if (clean.length > 2 && !stopWords.has(clean)) {
        if (clean.endsWith('s')) {
          wordSet.add(clean);  // keep plural only
        }
      }
    });
  });

  return JSON.stringify({
    phrases: Array.from(newUniquePhrases),
    words: Array.from(wordSet)
  });
})();

            ";

                try
                {
                    // Execute the JavaScript code in the WebView and get the result
                    string result = await webView.ExecuteScriptAsync(jsCode);
                    System.Diagnostics.Debug.WriteLine("Raw result: " + result); // Log the raw result to see if it's what we expect

                    // WebView returns a JSON-encoded string with quotes — we need to parse the string inside it
                    string innerJson = JsonDocument.Parse(result).RootElement.GetString();
                    System.Diagnostics.Debug.WriteLine("Inner JSON: " + innerJson);

                    if (string.IsNullOrEmpty(result))
                    {
                        System.Diagnostics.Debug.WriteLine("Received an empty result from the script.");
                        
                        return;
                    }

                    // Parse the result as JSON
                    var jsonResult = JsonDocument.Parse(innerJson);

                    // Log the type of the root element
                    var root = new Dictionary<string, JsonElement>();

                    foreach (var property in jsonResult.RootElement.EnumerateObject())
                    {
                        root[property.Name] = property.Value;
                    }






                
                    bool updated = false;

                    if (root.ContainsKey("phrases"))
                    {
                        var phrasesElement = root["phrases"];
                        System.Diagnostics.Debug.WriteLine("Phrases type: " + phrasesElement.ValueKind); // Log the type of 'phrases'

                        if (phrasesElement.ValueKind == JsonValueKind.Array)
                        {
                            updated = true;
                            var phrases = phrasesElement.EnumerateArray();
                            foreach (var phrase in phrases)
                            {
                                string phraseText = phrase.GetString();
                                if (phraseCounts.ContainsKey(phraseText))
                                    phraseCounts[phraseText]++;
                                else
                                    phraseCounts[phraseText] = 1;
                            }
                        }
                        else
                        {
                            System.Diagnostics.Debug.WriteLine("'phrases' is not an array. It is of type: " + phrasesElement.ValueKind);
                        }
                    }

                    // Check if 'phrases' exists and is an array


                    // Check if 'words' exists and is an array
                    if (root.ContainsKey("words"))
                        {
                            var wordsElement = root["words"];
                            System.Diagnostics.Debug.WriteLine("Words type: " + wordsElement.ValueKind); // Log the type of 'words'

                            if (wordsElement.ValueKind == JsonValueKind.Array)
                            {
                                var words = wordsElement.EnumerateArray();
                                foreach (var word in words)
                                {
                                    string wordText = word.GetString();
                                    if (wordCounts.ContainsKey(wordText))
                                        wordCounts[wordText]++;
                                    else
                                        wordCounts[wordText] = 1;
                                }
                            }
                            else
                            {
                                System.Diagnostics.Debug.WriteLine("'words' is not an array. It is of type: " + wordsElement.ValueKind);
                            }
                    }

                        // Check if scraping is complete by looking for a specific string in the result
                        if (result.Contains("--COMPLETE--"))
                        {
                            // Indicate that scraping is complete in the TextBox
                    
                        }

                    // If any update happened (i.e., we found phrases or words)
                    if (updated)
                    {
                        // Sort and display the word counts and phrase counts in the TextBox
                        var wordResults = string.Join(Environment.NewLine,
                            wordCounts.OrderByDescending(key => key.Value)
                            .Select(kv => $"{kv.Key}: {kv.Value}"));

                        var phraseResults = string.Join(Environment.NewLine,
                            phraseCounts.OrderByDescending(key => key.Value)
                            .Select(kv => $"{kv.Key}: {kv.Value}"));
                        wordsTextBox.Text = wordResults;
                        phrasesTextBox.Text = phraseResults;


                    }


                    
                    
                }
                catch (JsonException jsonEx)
                {
                    // Handle JSON parsing errors
                    System.Diagnostics.Debug.WriteLine("JSON Parsing Error: " + jsonEx.Message);
                    
                }
                catch (Exception ex)
                {
                    // Catch any other errors
                    System.Diagnostics.Debug.WriteLine("General Error: " + ex.Message);
                
                }
            };
            scrapeTimer.Start();

        }    
        
        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}

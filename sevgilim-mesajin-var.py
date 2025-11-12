import React, { useState } from 'react';
import { Heart, Mail } from 'lucide-react';

export default function LoveLetter() {
  const [isOpen, setIsOpen] = useState(false);
  const [showForm, setShowForm] = useState(false);
  const [recipient, setRecipient] = useState('Sevgilim');
  const [sender, setSender] = useState('Ben');
  const [customMessage, setCustomMessage] = useState('');
  const [generatedMessage, setGeneratedMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const defaultMessages = [
    `Sevgili ${recipient},

Seni gördüğüm ilk günden beri hayatım tamamen değişti. Her sabah senin yüzünü görmek, her gece seninle konuşmak benim günümü tamamlayan şey. 

Seninle geçirdiğim her an benim için bir hazine. Senin gülüşün, senin ses tonun, senin her hareketi beni daha çok sana yaklaştırıyor. Seninle olduğumda kendimi çok güvende ve sevili hissediyorum.

Sana söylemek istediğim şey çok basit: Seni çok seviyorum. Seninle bir gelecek hayal etmek benim için en güzel düşü.

Her zaman yanında olacağım, her adımında seninle yürüyeceğim.

Seninle sonsuza dek...

${sender}`,

    `Sevgili ${recipient},

Bu mektup sana bir gün yanağındaki o tebessümü nasıl kaybetsem korkan, seninle her anı yakalamak isteyen biri tarafından yazılıyor.

Seninle birlikte yaşadığımız anıların her biri benim kalbimde yazılı. Birlikte güldüğümüz, ağladığımız, hayalleri kurduğumuz her an bana değer verdi.

Hayatımda seninle olmak kadar doğru hiçbir şey yok. Sen benim ilham kaynağım, benim gücüm, benim umudum.

Seni sevgim, ışık hızı kadar hızlı, okyanuslar kadar derin, gökyüzü kadar sonsuz.

Seninle olmak için doğdum.

Sonsuz sevgiyle,
${sender}`,

    `Sevgili ${recipient},

Senin olmadığın bir dünyayı hayal edemiyorum artık. Seninle tanıştığım günden beri hayatım anlam kazandı, renklendi, yaşanmaya başladı.

Her sabah seni düşünerek uyanıyorum, her gece seninle düşlerimi görüyorum. Seninle konuşurken zaman duruveriyor, etrafındaki her şey kayboluveriyor, sadece sen varsın.

Sana verdiğim söz, seni her zaman sevmek ve değer vermektir. Güneş doğduğu sürece, yıldızlar gökyüzünde parladığı sürece, sen benim kalbimde her zaman özel olacaksın.

Teşekkür ederim, seni sevdiğim için bu iyi şans için.

Sonsuza dek seninle,
${sender}`
  ];

  const generateMessage = async () => {
    if (!customMessage.trim()) return;
    
    setIsLoading(true);
    try {
      const response = await fetch('https://api.anthropic.com/v1/messages', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          model: 'claude-sonnet-4-20250514',
          max_tokens: 1000,
          messages: [
            {
              role: 'user',
              content: `${recipient} için romantik bir mektup yazınız. Gönderen: ${sender}. 
              
Mektubun ana mesajı: ${customMessage}

Türkçe yazınız. Samimi, duygusal ama doğal olsun. Çok abartılı olmasın. Sadece mektup metnini yazınız, başka hiçbir şey yazmasın.`
            }
          ]
        })
      });

      const data = await response.json();
      const message = data.content[0].text;
      setGeneratedMessage(message);
      setIsOpen(true);
      setShowForm(false);
    } catch (error) {
      console.error('Hata:', error);
      alert('Mektup oluşturulamadı. Lütfen tekrar deneyin.');
    } finally {
      setIsLoading(false);
    }
  };

  const currentMessage = generatedMessage || defaultMessages[0];

  return (
    <div className="min-h-screen bg-gradient-to-br from-red-50 via-pink-50 to-rose-50 flex items-center justify-center p-4">
      <div className="max-w-2xl w-full">
        {!isOpen && !showForm && (
          <div className="text-center">
            <div className="mb-8">
              <Mail className="w-24 h-24 mx-auto text-rose-500 mb-4" />
              <h1 className="text-4xl font-bold text-gray-800 mb-2">Sana Bir Mesajım Var</h1>
              <p className="text-gray-600 mb-8">Mektupunuzu açmak için tıklayın...</p>
            </div>
            
            <button
              onClick={() => setIsOpen(true)}
              className="bg-gradient-to-r from-red-500 to-rose-500 hover:from-red-600 hover:to-rose-600 text-white px-8 py-4 rounded-full text-xl font-bold transform hover:scale-105 transition-all shadow-lg mb-4 flex items-center justify-center gap-2 mx-auto"
            >
              <Heart className="w-6 h-6" />
              Mektup Aç
            </button>

            <button
              onClick={() => setShowForm(true)}
              className="bg-white border-2 border-rose-500 text-rose-500 hover:bg-rose-50 px-6 py-3 rounded-full font-semibold transition-all mx-auto block"
            >
              Kişisel Mesaj Oluştur
            </button>
          </div>
        )}

        {showForm && (
          <div className="bg-white rounded-2xl shadow-2xl p-8 border-2 border-rose-200">
            <h2 className="text-2xl font-bold text-gray-800 mb-6">Kişisel Mektup Oluştur</h2>
            
            <div className="mb-4">
              <label className="block text-gray-700 font-semibold mb-2">Sevgilinin Adı</label>
              <input
                type="text"
                value={recipient}
                onChange={(e) => setRecipient(e.target.value)}
                className="w-full border-2 border-gray-300 rounded-lg p-3 focus:outline-none focus:border-rose-500"
                placeholder="Sevgilinin adı"
              />
            </div>

            <div className="mb-4">
              <label className="block text-gray-700 font-semibold mb-2">Senin Adın</label>
              <input
                type="text"
                value={sender}
                onChange={(e) => setSender(e.target.value)}
                className="w-full border-2 border-gray-300 rounded-lg p-3 focus:outline-none focus:border-rose-500"
                placeholder="Senin adın"
              />
            </div>

            <div className="mb-6">
              <label className="block text-gray-700 font-semibold mb-2">Mesajın Ana Konusu</label>
              <textarea
                value={customMessage}
                onChange={(e) => setCustomMessage(e.target.value)}
                className="w-full border-2 border-gray-300 rounded-lg p-3 focus:outline-none focus:border-rose-500 h-32 resize-none"
                placeholder="Ör: Onunla geçirdiğim güzel anılar, onun bana kattığı değer, gelecek hayallerimiz..."
              />
            </div>

            <div className="flex gap-4">
              <button
                onClick={generateMessage}
                disabled={isLoading || !customMessage.trim()}
                className="flex-1 bg-gradient-to-r from-red-500 to-rose-500 hover:from-red-600 hover:to-rose-600 disabled:opacity-50 text-white py-3 rounded-lg font-bold transition-all"
              >
                {isLoading ? 'Mektup Yazılıyor...' : 'Mektup Oluştur'}
              </button>
              <button
                onClick={() => setShowForm(false)}
                className="flex-1 bg-gray-200 hover:bg-gray-300 text-gray-800 py-3 rounded-lg font-bold transition-all"
              >
                İptal
              </button>
            </div>
          </div>
        )}

        {isOpen && (
          <div className="relative">
            <div className="bg-amber-50 border-4 border-amber-900 rounded-lg p-12 shadow-2xl transform transition-all duration-500 hover:shadow-3xl"
                 style={{ 
                   backgroundImage: 'repeating-linear-gradient(90deg, transparent, transparent 2px, rgba(0,0,0,.03) 2px, rgba(0,0,0,.03) 4px)',
                   minHeight: '500px'
                 }}>
              <Heart className="w-8 h-8 text-rose-500 mx-auto mb-6" />
              
              <div className="text-gray-800 text-lg leading-relaxed font-serif whitespace-pre-wrap mb-8">
                {currentMessage}
              </div>

              <div className="flex gap-4 justify-center pt-6 border-t-2 border-amber-200">
                <button
                  onClick={() => setIsOpen(false)}
                  className="bg-gray-500 hover:bg-gray-600 text-white px-6 py-2 rounded-lg font-semibold transition-all"
                >
                  Kapat
                </button>
                {generatedMessage && (
                  <button
                    onClick={() => {
                      setShowForm(true);
                      setGeneratedMessage('');
                    }}
                    className="bg-rose-500 hover:bg-rose-600 text-white px-6 py-2 rounded-lg font-semibold transition-all"
                  >
                    Başka Mesaj Oluştur
                  </button>
                )}
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

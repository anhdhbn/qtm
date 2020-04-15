from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
  return "hello world!"

@app.route('/stress-test/<limit>')
def stress_test(limit=10):
  return str(generate_n_primes(int(limit)))

def generate_n_primes(N):
  primes  = []
  chkthis = 2
  while len(primes) < N:
    ptest    = [chkthis for i in primes if chkthis%i == 0]
    primes  += [] if ptest else [chkthis]
    chkthis += 1
  return primes

if __name__ == '__main__':
  app.run()
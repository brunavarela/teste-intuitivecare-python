<template>
  <div class="form-container">
    <form @submit.prevent="buscarOperadoras">
      <input 
        v-model="termoBusca" 
        type="text" 
        placeholder="Buscar operadora" 
        required 
      />
      <button type="submit">Buscar</button>
    </form>

    <div class="container-list" v-if="operadoras.length">
      <ul>
        <li v-for="operadora in operadoras" :key="operadora.id">
          <strong>{{ operadora.razao_social }}</strong><br>
          CNPJ: {{ operadora.cnpj }}<br>
          Registro ANS: {{ operadora.registro_ans }}
        </li>
      </ul>
    </div>

    <div v-else-if="erro">
      <p class="erro">{{ erro }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      termoBusca: '',
      operadoras: [],
      erro: '',
    };
  },
  methods: {
    async buscarOperadoras() {
      this.erro = ''; 
      this.operadoras = []; 

      try {
        const response = await axios.get(`http://localhost:5000/buscar_operadoras?termo=${this.termoBusca}`);

        if (response.data.length > 0) {
          this.operadoras = response.data;
        } else {
          this.erro = 'Desculpe. Nenhuma operadora encontrada com este termo.';
        }
      } catch (error) {
        this.erro = 'Erro ao buscar operadoras. Tente novamente.';
        console.error(error);
      }
    },
  },
};
</script>

<style scoped>
  .form-container {
    width: 100%;
  }

  form {
    margin-bottom: 40px;
    display: flex;
    flex-direction: column;
    gap: 20px;
  }

  input {
    padding: 8px;
    background: transparent;
    border: none;
    border-bottom: 1px solid #24D995 !important;
    text-align: left;
    color: white;
  }

  input:focus {
    outline: none;
    border-bottom: 1px solid #02E883 !important;
  }

  button {
    padding: 8px;
    background: #24D995;
    color: black;
    font-weight: 700;
    text-transform: uppercase;
    border: none;
    border-radius: 4px;
    font-size: 14px;
    height: 40px;
    cursor: pointer;
  }

  button:hover {
    background: #02E883;
  }

  ul {
    list-style-type: none;
    padding-left: 0;
    max-height: 350px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    overflow: auto;
  }

  li {
    background: #12171B;
    padding: 16px;
    display: flex;
    flex-direction: column;
    text-align: left;
    border-radius: 4px;
    border: 0.5px solid #24D995;
  }

  .erro {
    color: white;
    text-align: center;
    font-weight: 500;
    margin-top: 10px;
  }

  @media screen and (min-width: 768px) {
    .form-container {
      display: flex;
      flex-direction: column;
      justify-content: center;align-items: center;
      margin-top: 20px;
    }

    form {
      flex-direction: row;
      justify-content: center;
      min-width: 500px;
    }

    input {
      width: 360px;
    }

    button {
      width: 120px
    }
    
    .container-list {
      max-width: 900px
    }

    ul {
      flex-direction: row;
      justify-content: center;
      flex-wrap: wrap;
      max-height: 300px;
    }

    li {
      min-width: 400px;
      width: 400px;
    }
  }

  ::-webkit-scrollbar {
    width: 1px;
  }
  ::-webkit-scrollbar-thumb {
    background: #02E883;
  }

  @media screen and (min-width: 1400px) {
    ul {
      max-height: 500px;
    }
  }
</style>

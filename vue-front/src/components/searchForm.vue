<template>
  <div>
    <h2>Buscar Operadoras</h2>
    <form @submit.prevent="buscarOperadoras">
      <input 
        v-model="termoBusca" 
        type="text" 
        placeholder="Digite o nome da operadora" 
        required 
      />
      <button type="submit">Buscar</button>
    </form>
    <div v-if="operadoras.length">
      <h3>Resultados:</h3>
      <ul>
        <li v-for="operadora in operadoras" :key="operadora.id">
          <strong>{{ operadora.razao_social }}</strong><br>
          CNPJ: {{ operadora.cnpj }}<br>
          Registro ANS: {{ operadora.registro_ans }}
        </li>
      </ul>
    </div>
    <div v-else-if="erro">
      <p>{{ erro }}</p>
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
      this.erro = '';  // Limpar erro anterior
      try {
        const response = await axios.get(`http://localhost:5000/buscar_operadoras?termo=${this.termoBusca}`);
        this.operadoras = response.data;
      } catch (error) {
        this.erro = 'Erro ao buscar operadoras. Tente novamente.';
        console.error(error);
      }
    },
  },
};
</script>

<style scoped>
h2 {
  margin-bottom: 10px;
}
form {
  margin-bottom: 20px;
}
input {
  padding: 8px;
  margin-right: 10px;
}
button {
  padding: 8px;
}
ul {
  list-style-type: none;
  padding-left: 0;
}
li {
  margin-bottom: 10px;
}
</style>

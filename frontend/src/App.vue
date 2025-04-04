<template>
  <div class="container">
    <h1>Buscar Operadoras de Saúde</h1>
    <input
      v-model="termo"
      @input="buscarOperadoras"
      placeholder="Digite o nome da operadora"
    />
    <div v-if="carregando">Carregando...</div>
    <ul v-else>
      <li v-for="(operadora, index) in resultados" :key="index">
        {{ operadora["Razao_Social"] || "Sem nome" }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      termo: "",
      resultados: [],
      carregando: false,
    };
  },
  methods: {
    async buscarOperadoras() {
      if (this.termo.length < 2) {
        this.resultados = [];
        return;
      }

      this.carregando = true;
      try {
        const response = await fetch(`http://localhost:5000/buscar?termo=${this.termo}`);
        this.resultados = await response.json();
      } catch (error) {
        console.error("Erro na busca:", error);
      } finally {
        this.carregando = false;
      }
    },
  },
};
</script>

<style>
.container {
  max-width: 600px;
  margin: auto;
  padding: 2rem;
  font-family: Arial, sans-serif;
}
input {
  width: 100%;
  padding: 0.5rem;
  margin-bottom: 1rem;
  font-size: 1rem;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  background: #f5f5f5;
  margin-bottom: 0.5rem;
  padding: 0.5rem;
  border-radius: 5px;
}
</style>

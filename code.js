fetch('data.json', {mode: 'no-cors'})
  .then(function(res) {
    return res.json()
  })
  .then(function(data) {
    var cy = window.cy = cytoscape({
      container: document.getElementById('cy'),

      boxSelectionEnabled: false,
      autounselectify: true,

      layout: {
        name: 'breadthfirst',
		directed: true,
		padding: 10,
        animate: false
      },

      style: [
        {
          selector: 'node',
          style: {
			'shape': 'roundrectangle',
            'background-color': '#d5fcd7',
            'border-color': 'black',
            'border-width': 1,
			'width': 80,
			'height': 40,
			'text-valign': 'center',
			'font-size': 12,
			'label': 'data(name)'
          }
        },

        {
          selector: 'node.rxn',
          style: {
			'shape': 'rectangle',
            'background-color': 'white',
			'width': 10,
			'height': 10,
			'label': ''
          }
        },

        {
          selector: 'edge',
		  style: {
			'curve-style': 'bezier',
            'width': 1,
			'target-arrow-shape': 'triangle',
			'arrow-scale': 1.3,
			'line-color': 'black',
			'target-arrow-color': 'black'
          }
        },

        {
          selector: 'edge.activation',
		  style: {
			'target-arrow-shape': 'circle',
			'arrow-scale': 0.8,
			'target-arrow-fill': 'hollow',
			'line-style': 'dotted'
          }
        },

        {
          selector: 'edge.inhibition',
		  style: {
			'target-arrow-shape': 'tee',
			'arrow-scale': 0.8,
			'line-style': 'dashed'
          }
        },

        {
          selector: 'edge.reactant',
		  style: {
			'target-arrow-shape': 'none',
          }
        }
      ],

      elements: data
    });
  });

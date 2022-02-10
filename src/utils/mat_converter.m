dirpath='teeth';
dirpath1='teeth_pics';
type='mat';
type1='png';
oldvar = '';
for j=1:12
    infile = fullfile(dirpath, sprintf('set%d.mat', j));
    outfile = fullfile(dirpath1, sprintf('set%d.jpg', j));
    datastruct = load(infile);
    fn = fieldnames(datastruct);
    firstvar = fn{1};
    data = datastruct.(firstvar);
    imwrite( data, outfile );
    if ~strcmp(oldvar, firstvar)
      fprintf('loading from variable %s as of file %d\n', firstvar);
    end
end
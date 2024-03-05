package repository;

import domain.Identifiable;

public abstract class FileRepository<T extends Identifiable, U> extends MemoryRepository<T,U> {

    protected String fileName;

    public FileRepository(String fileName) {
        this.fileName = fileName;
        readFromFile();
    }

    protected abstract void readFromFile();
    protected abstract void writeToFile();
    @Override
    public void add(T item)
    {
        super.add(item);
        writeToFile();


    }
    @Override
    public void remove(Integer item)
    {
       super.remove(item);
        writeToFile();

    }
}